"""
Integration of Chung2 dataset
"""

import os
import numpy as np
# from keras.preprocessing.image import load_img, img_to_array
# from tqdm.notebook import tqdm
from Dataset import Dataset
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Conda Installation: conda install -c bokeh bokeh
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import CustomJS, HoverTool, PanTool, WheelZoomTool
from bokeh.models.widgets import Button
from bokeh.layouts import widgetbox, gridplot, column, row

# Conda Installation: conda install pandas
import pandas as pd

chung2 = Dataset(
    "chung2-actualmed",
    os.path.join(os.getcwd() + "\data"),
    extras="\\images\\",
    metadata_fn="metadata.csv",
    class_headers=("imagename", "finding")
)
