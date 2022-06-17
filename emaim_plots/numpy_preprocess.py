"""
This code here is based off the following Python Notebook:
https://github.com/zeeshannisar/COVID-19/blob/master/datasets/Read%20Dataset%20and%20Make%20Numpy%20Files.ipynb
"""

import os
import numpy as np
# from keras.preprocessing.image import load_img, img_to_array
# from tqdm.notebook import tqdm

# Change OS current directory to where the images are stored.

# os.chdir(os.path.join(cwd)) # Change OS directory to parent directory of where data is stored
dataDir = "./data"
# directories = os.listdir("./data") # List all items in the current directory

def get_dataset_classes():
    """
    Return list of directories in cwd/dataDir, rejecting non-directory entries.
    Assumes that folder structure is dataset1/class1, dataset1/class2 etc
    """
    return [ds for ds in os.listdir(dataDir) if os.path.isdir(cwd + dataDir + ds)]

def img_to_numpy_save(directory):
    """
    The goal of this method is to convert the images to the .npy format required for the bokeh plots.
    :str directory: Directory for each class.
    """
    images = []
    classes = []

    classes = os.listdir(".")

    print(classes)

if __name__ == "__main__":
    cwd = os.getcwd() # /repo/emaim_plots -> emaim_plots/data/mooney/test
    print(cwd)
    goto = cwd + r"\data\mooney\test"
    print("Going to: "+ goto)
    os.chdir(goto)
    img_to_numpy_save(dir)
