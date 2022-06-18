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
            return dicom_image

        else:
            images = []
            filenames = [fn for fn in os.listdir(os.getcwd()) if fn.endswith(('.dcm', '.dicom'))]

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

        if metadata_fn == None:
            # List of strings, representing dataset classes.
            self.classes = os.listdir(basePath + extras)
            print("Classes are: " + str(self.classes))

        else:
            metadata = pd.read_csv(basePath + "\\" + metadata_fn)
            self.classes = metadata['class'].unique()
            print("Classes are: " + str(self.classes))

        # Load the images
        for class_num, c in enumerate(self.classes):
            # For each class directory, we want to load the images:
            classPath = basePath + extras + "\\" + c
            if metadata_fn == None:
                c_filenames = os.listdir(classPath)
            else:
                c_filenames = os.listdir(basePath + extras)
            c_images = []

            self.distributions[c] = len(c_filenames)

            if c_filenames[0].endswith(('.dcm', 'dicom')):
                self.images = Dataset.load_dicom(abs_fp)
            else:
                # PIL Image
                for filename in c_filenames:
                    if (metadata_fn) == None:
                        image_fp = classPath + "\\" + filename
                    else:
                        image_fp = basePath + extras + "\\" + filename
                    image = np.asarray(Image.open(classPath + "\\" + filename))
                    image_crop = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
                    self.images.append(image_crop)
                    self.labels.append(class_num)
        self.images_flat = []
        # self.images_flat = np.reshape(self.images, (len(self.images), 224*224))
        for im in self.images:
            self.images_flat.append(np.reshape(im, (224*224)))

            # plt.imshow(self.images[0])
            # plt.show()
