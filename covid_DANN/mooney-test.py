import os
from data import MooneyDataset
import cv2

mooney = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\mooney\\metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\mooney\\images"
)

for sample in mooney:
    image = sample['image']
    diagnosis = sample['diagnosis']
    image_name = sample['filename']
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    break
