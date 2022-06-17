"""
======= DISCONTINUED ? =======
======= DISCONTINUED ? =======
======= DISCONTINUED ? =======
======= DISCONTINUED ? =======
======= DISCONTINUED ? =======



This code here is based off the following Python Notebook:
https://github.com/zeeshannisar/COVID-19/blob/master/datasets/Read%20Dataset%20and%20Make%20Numpy%20Files.ipynb
"""

import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from tqdm.notebook import tqdm

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

    currentPath = os.path.join(dataDir, directory)
    classes = os.listdir(currentPath)
    # If the next level is test / train / validate, just use the test dataset.
    if 'test' in classes:
        currentPath = os.path.join(dataDir, directory, './test')
        classes = os.listdir(currentPath)
        # Firstly, get the image names:

    print(f"Directory: {directory}, Classes: {classes}")

    for i, c in enumerate(classes):
        # i is the class index, e.g. if classes = ['PNEUMONIA', 'NORMAL']
        # then if c = 'PNEUMONIA', i = 0 and if c = 'NORMAL' then i = 1

        print(f"Reading data for class {c}")
        classPath = os.path.join(currentPath + "./" + c)
        imageNames = os.listdir(classPath)
        for imgName in imageNames:
            img = load_img(
                os.path.join(classPath, imgName),
                target_size = (224, 224),
                color_mode='rgb',
                interpolation='lanczos'
            )

            imgArray = img_to_array(img, data_format='channels_last', dtype='float32')
            images.append(imgArray)
            labels.append(i) # Class index

    images = np.array(images).reshape(-1, 224, 224, 3)
    print("{directory} Data: {images.shape}")
    labels = np.array(labels)
    print("{directory} Labels: {labels.shape}")
    np.save(dataDir + directory + "_images", images)

if __name__ == "__main__":
    # We want the current directory to be the folder containing all of the datasets.
    cwd = os.getcwd() # /repo/emaim_plots -> emaim_plots/data/mooney/test
    print(cwd)
    # goto = cwd + r"\data\mooney\test"
    # print("Going to: "+ goto)
    os.chdir(cwd)
    img_to_numpy_save("mooney")
