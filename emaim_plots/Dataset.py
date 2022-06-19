import os
# Conda Installation: conda install -c conda-forge imageio
import PIL.Image as Image # To import images from filepath
# Conda Installation: conda install -c conda-forge matplotlib
import numpy as np
import matplotlib.pyplot as plt
# Conda Installation: conda install -c conda-forge opencv
import cv2
# Conda Installation: conda install -c conda-forge pydicom
import pydicom
# Conda Installation: conda install pandas
import pandas as pd
class Dataset:
    def load_dicom(abs_fp, name=None):
        """
        Static class method used to load .dcm images using PyDiCom.
        Installed v2.3.0 using conda install -c conda-forge pydicom(=2.3.0)

        :str abs_fp:       Absolute filepath to root dataset folder
        :str (name):       Optional parameter. If name = None, load all images in folder
                               and return as a list.
                           Else, just load and return that single image
        """

        if (name != None):
            # Load single image
            dicom_image = pydicom.read_file(abs_fp + "/" + name)
            return dicom_image.pixel_array

        else:
            images = []
            # print(os.listdir(abs_fp))
            filenames = [fn for fn in os.listdir(abs_fp) if fn.endswith(('.dcm', '.dicom'))]
            # print(f"DICOM Filenames: {filenames}")

            for fn in filenames:
                dicom_image = pydicom.read_file(abs_fp + "/" + fn)
                images.append(dicom_image.pixel_array)
            return images

    def __init__(self, dataset_name, abs_fp, metadata_fn=None, extras=None):
        """
        Construct a new instance of the dataset used for the Bokeh plot.
        :str dataset_name: Used to find the dataset files.
        :str abs_fp:          Absolute filepath to root dataset folder
        :str (extras):        Extra directories after dataset_name
        :str (metadata_fn):   Name of metadata file, in directory abs_fp

        Will look for dataset source files at `abs_fp + dataset_name + extras`
        E.g., if abs_fp = "C:\\Users\\$username\\Documents\\CovidX\\data"
                 dataset_name = "mooney"
                 extras = "\\test"
        """
        print("\tDataset name is " + dataset_name)
        basePath = abs_fp + "\\" + dataset_name
        self.distributions = dict() # Dictionary of class names : counts
        self.labels = []
        self.images = []
        self.filenames = []

        if metadata_fn == None:
            """
            Load without a metadata file, i.e. classes are divided using folders.
            """
            # List of strings, representing dataset classes.
            self.classes = os.listdir(basePath + extras)
            print("Classes are: " + str(self.classes))

            # Since classes are divided by folders, we want to add them class by class:
            # Load the images
            for class_num, c in enumerate(self.classes):
                # For each class directory, we want to load the images:
                classPath = basePath + extras + "\\" + c
                c_filenames = os.listdir(classPath)

                c_images = []

                self.distributions[c] = len(c_filenames)

                if c_filenames[0].endswith(('.dcm', 'dicom')):
                    images = Dataset.load_dicom(classPath)
                    print(f"Loaded {len(self.images)} images from DICOM format.")
                    self.images = [
                        cv2.resize(im, dsize=(224,224), interpolation=cv2.INTER_CUBIC) for im in images
                    ]
                else:
                    # PIL Image
                    for filename in c_filenames:
                        image_fp = classPath + "\\" + filename
                        image = np.asarray(Image.open(image_fp))
                        image_crop = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
                        self.images.append(image_crop)
                        self.labels.append(class_num)
                self.filenames += [classPath + "\\" + fn for fn in c_filenames]

        else:
            """
            Load using a metadata file.
            """
            metadata = pd.read_csv(basePath + "\\" + metadata_fn)
            self.classes = metadata['class'].unique()
            path = basePath + extras
            print("Classes are: " + str(self.classes))

            c_filenames = os.listdir(path)

            if c_filenames[0].endswith(('.dcm', 'dicom')):
                images = Dataset.load_dicom(path)
                self.images = [
                    cv2.resize(im, dsize=(224,224), interpolation=cv2.INTER_CUBIC) for im in images
                ]
                print(f"\tLoaded {len(self.images)} images from DICOM format from {path}.")
            else:
                # PIL Image
                for filename in c_filenames:
                    image_fp = path + "\\" + filename
                    image = np.asarray(Image.open(path + "\\" + filename))
                    image_crop = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
                    self.images.append(image_crop)
                    self.labels.append(class_num)
            self.filenames += [basePath + "\\export\\" + fn.split(".")[0] + ".png" for fn in c_filenames]

            # Now need to add the labels.
            classMap = dict()
            for num, name in enumerate(self.classes):
                classMap[name] = num
            for fn in c_filenames:
                # print(metadata.loc[metadata['patientId']==fn.split(".")[0]]['class'])
                if fn.endswith((".dcm", ".dicom")):
                    self.labels.append(
                        metadata.loc[metadata['patientId']==fn.split(".")[0]]['class']
                    )
        print("Number of labels: " + str(len(self.labels)))

        self.images_flat = []
        for im in self.images:
            self.images_flat.append(np.reshape(im, (224*224)))

        print("Number of images: " + str(len(self.images_flat)))
