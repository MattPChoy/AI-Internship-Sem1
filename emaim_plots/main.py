"""
Step 1: Load images using NumPy
"""
# Tensorflow: conda install -c conda-forge tensorflow=1.14.0
import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from tqdm.notebook import tqdm
