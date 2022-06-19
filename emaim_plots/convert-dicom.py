from Dataset import Dataset
import os
import cv2

fp = os.getcwd() + "\\data\\rsna-pneumonia-detection-challenge\\train\\"
filenames = [fn for fn in os.listdir(fp) if fn.endswith(('.dcm', '.dicom'))]

for fn in filenames:
    image = Dataset.load_dicom(fp, fn)
    cv2.imwrite(fn.split(".")[0] + ".png", image)
