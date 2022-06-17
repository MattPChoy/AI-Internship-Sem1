"""
Step 1: Load images using NumPy
"""
# Conda Installation: conda install -c conda-forge tensorflow=1.14.0
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

"""
For Mooney:
"""
mooney = Dataset(
    "mooney",
    os.path.join(os.getcwd() + "\data"),
    extras="\\test"
)

model = TSNE(n_components=2, init='pca')
print(np.shape(mooney.images_flat))
X_embedded = model.fit_transform(mooney.images_flat)

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)
ax.scatter(X_embedded[:,0], X_embedded[:,1], s=25)

"""
For Bokeh
"""
# Construct the Pandas DataFrame that will hold the data that we want to plot.

output_file("./bokeh_mooney.html")
figure_size = 500

p = figure(tools=[PanTool(), WheelZoomTool()],
    plot_width=figure_size + 500, plot_height=figure_size,
    toolbar_location="above", title="Mooney Bokeh Analysis"
)

#p.circle('x_val', 'y_val', fill_color='color_data', source=source, line_color='black', size=10, alpha=0.7)
p.circle(X_embedded[:,0], X_embedded[:,1])
show(p)
