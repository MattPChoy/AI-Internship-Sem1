import os
from data import RSNADataset
import cv2

train_rsna = RSNADataset(
    csv_file = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\train_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\train"
)

test_rsna = RSNADataset(
    csv_file = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\test_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\train"
)

for i in train_rsna:
    im = i['image']
    diag = i['diagnosis']
    fn = i['filename']

    cv2.imshow(fn.split("\\")[-1] + " - " + diag, im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    break

for i in test_rsna:
    im = i['image']
    diag = i['diagnosis']
    fn = i['filename']

    cv2.imshow(fn.split("\\")[-1] + " - " + str(diag), im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    break
