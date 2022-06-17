import os
# Conda Installation: conda install -c conda-forge imageio
import PIL.Image as Image # To import images from filepath
# Conda Installation: conda install -c conda-forge matplotlib
import numpy as np
import matplotlib.pyplot as plt
# Conda Installation: conda install -c conda-forge opencv
import cv2
class Dataset:
    def __init__(self, dataset_name, abs_fp, metadata_fp = None, extras=None):
        """
        :str dataset_name: Used to find the dataset files.
        :str abs_fp:       Absolute filepath to root dataset folder
        :str (extras):     Extra directories after dataset_name

        Will look for dataset source files at `abs_fp + dataset_name + extras`
        E.g., if abs_fp = "C:\\Users\\$username\\Documents\\CovidX\\data"
                 dataset_name = "mooney"
                 extras = "\\test"
        """
        print("\tDataset name is " + dataset_name)

        if metadata_fp == None:
            # List of strings, representing dataset classes.
            basePath = abs_fp + "\\" + dataset_name + extras
            self.classes = os.listdir(abs_fp + "\\" + dataset_name + extras)
            self.labels = []
            self.images = []
            self.distributions = dict() # Dictionary of class names : counts
            print("Classes are: " + str(self.classes))

            for class_num, c in enumerate(self.classes):
                # For each class directory, we want to load the images:
                classPath = basePath + "\\" + c
                c_filenames = os.listdir(classPath)
                c_images = []

                self.distributions[c] = len(c_filenames)

                # PIL Image
                for filename in c_filenames:
                    image = np.asarray(Image.open(classPath + "\\" + filename))
                    image_crop = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
                    self.images.append(image_crop)
                    self.labels.append(class_num)
                    # print(np.shape(self.images[-1]))

                # plt.imshow(self.images[0])
                # plt.show()

            self.images_flat = []
            # self.images_flat = np.reshape(self.images, (len(self.images), 224*224))
            for im in self.images:
                self.images_flat.append(np.reshape(im, (224*224)))
        else:
            raise Exception("Creating Bokeh dataset from metadata file not supported yet.")
