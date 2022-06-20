from torch.utils.data import SubsetRandomSampler, DataLoader, Dataset
import pandas as pd
from .Loader import Loader
import torch
import numpy as np
import os
import cv2

class Mooney(Loader):
    MEAN = 0.5
    STDEV = 0.5

    def __init__(self, mean=MEAN, stdev=STDEV):
        super().__init__(mean, stdev)


class MooneyDataset(Dataset):
    """
    Downloaded from kaggle:
    https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
    """

    def __init__(self, csv_file, root_dir, transform=None):
        """
        :str csv_file:  Path to the CSV file with annotations
        :str root_dir:  Directory with all of the images
        : (transform):  Optional transform to be applied on a sample.
        """

        self.transform = transform
        self.metadata = pd.read_csv(csv_file)
        self.root_dir = root_dir

    def __len__(self):
        """
        Returns the size of the dataset.
        """
        return len(self.metadata)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir,
                                self.metadata.iloc[idx, 0])
        image = cv2.imread(img_name)
        diagnosis = self.metadata.iloc[idx, 1:]
        sample = {'image': image, 'diagnosis': diagnosis, 'filename': img_name}

        if self.transform:
            sample = self.transform(sample)

        return sample
