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
For RSNA Pneumonia Detection Challenge from Kaggle
"""
rsna = Dataset(
    "rsna-pneumonia-detection-challenge",
    os.path.join(os.getcwd() + "\data"),
    extras="\\train",
    metadata_fn="stage_2_detailed_class_info.csv",
    class_header=("patientId", "class")
)
print(f"RSNA has {len(rsna.images_flat)} samples")

"""
For Mooney:
"""
mooney = Dataset(
    "mooney",
    os.path.join(os.getcwd() + "\data"),
    extras="\\test",
)
print(f"Mooney has {len(mooney.images_flat)} samples")

"""
For Chung2
"""
chung2 = Dataset(
    "chung2-actualmed",
    os.path.join(os.getcwd() + "\data"),
    extras="\\images\\",
    metadata_fn="metadata.csv",
    class_header=("imagename", "finding")
)

"""
TSNE
"""
model = TSNE(n_components=2, init='pca')
print(np.shape(mooney.images_flat))
X_embedded = model.fit_transform(mooney.images_flat + rsna.images_flat + chung2.images_flat)
print("Added " + str(len(X_embedded)) + " samples to the t-SNE plot")

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111)
ax.scatter(X_embedded[:,0], X_embedded[:,1], s=25)

"""
For Bokeh
"""
# Construct the Pandas DataFrame that will hold the data that we want to plot.

output_file("./bokeh_mooney.html")
figure_size = 500

hover = HoverTool(
    tooltips="""
        <div>
            <img
                src="file://@filepaths" alt="@base_filepaths" height="208" width="176"
                style="float: center;"
                border="2"
            ></img>
        </div>
        """
)

p = figure(tools=[PanTool(), WheelZoomTool(), hover],
    plot_width=figure_size + 500, plot_height=figure_size,
    toolbar_location="above", title="Mooney vs RSNA Competition - t-SNE Analysis"
)

def clamp(x):
    return max(0, min(x, 255))

def set_colors(vals_for_color):
    #print(vals_for_color)
    min_val = min(vals_for_color); max_val = max(vals_for_color)
    vals_for_color_norm = [(float(val) - min_val) / (max_val - min_val) for val in vals_for_color] #between 0 and 1
    vals_for_color_norm = [val if val<1 else 0.9999 for val in vals_for_color_norm]
    #print(vals_for_color_norm)
    colors_unit = [plt.cm.seismic(val)[:3] for val in vals_for_color_norm]
    #print(colors_unit)
    colors_rgb = [(int(color[0]*255), int(color[1]*255), int(color[2]*255)) for color in colors_unit]
    #print(colors_rgb)
    colors_hex = ["#{0:02x}{1:02x}{2:02x}".format(clamp(color_rgb[0]), clamp(color_rgb[1]), clamp(color_rgb[2])) for color_rgb in colors_rgb]

    #colors_hex = ['#' + struct.pack('BBB',*color_rgb).encode('hex') for color_rgb in colors_rgb]
    return colors_hex

print("Adding " + str(len(mooney.filenames + rsna.filenames)) + " to the dataframe for plot.")
df = pd.DataFrame.from_dict({
    'x_val': X_embedded[:,0],
    'y_val': X_embedded[:,1],
    'filepaths': mooney.filenames + rsna.filenames + chung2.filenames
})
# df['color'] = set_colors(mooney.labels + rsna.labels)
df['color'] = set_colors([0] * len(mooney.labels) + [1] * len(rsna.labels) + [2] * len(chung2.labels))

p.circle('x_val', 'y_val', fill_color='color', source=df, line_color='black', size=10, alpha=0.7)
# p.circle(X_embedded[:,0], X_embedded[:,1])
show(p)
# print(df.to_string())
