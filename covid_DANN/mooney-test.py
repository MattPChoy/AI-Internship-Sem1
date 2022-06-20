import os
from data import MooneyDataset
import cv2

test_mooney = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\mooney\\test_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\mooney\\images"
)

train_mooney = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\mooney\\train_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\mooney\\images"
)

print(f"The Mooney training dataset has {len(train_mooney)} entries")
print(f"The Mooney testing dataset has  {len(test_mooney)} entries")
