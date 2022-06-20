import os
from data import MooneyDataset
import cv2

mooney = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\stage_2_detailed_class_info.csv",
    root_dir = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\test"
)
