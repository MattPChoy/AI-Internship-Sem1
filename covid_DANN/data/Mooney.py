from torch.utils.data import SubsetRandomSampler, DataLoader, Dataset
import pandas as pd
from .Loader import Loader
import torch
import numpy as np
import os
import cv2

class MooneyLoader(Loader):
    """
    Dataloader for Mooney dataset.
    """
    MEAN = 0.5
    STDEV = 0.5

    def __init__(self, mean=MEAN, stdev=STDEV):
        super().__init__(mean, stdev)


class MooneyDataset(Dataset):
    """
    Subclass of PyTorch Dataset. Source downloaded from Kaggle.
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
        self.map = MooneyDataset.parse_csv(csv_file)
        self.filenames = sorted(self.map.keys())

        self.classes = self.metadata['class'].unique()
        self.class_map = {name : idx for idx, name in enumerate(self.classes)}

    def parse_csv(fp, sep=","):
        header = -1
        data = dict()
        with open(fp, "r") as csv_file:
            if header == -1:
                header = [h.strip() for h in csv_file.readline().split(sep)]
                # print(f"Headers are: {header}")
            for line in csv_file:
                line = [part.strip() for part in line.split(sep)[:2]]
                data[line[0]] = line[1]
        return data

    def __len__(self):
        """
        Returns the size of the dataset.
        """
        return len(self.metadata)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = self.filenames[idx]
        image_fp = self.root_dir + "\\" + img_name

        image = cv2.imread(image_fp)
        image = cv2.resize(image, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
        # diagnosis = self.metadata.iloc[idx, 1:]
        diagnosis = self.map[img_name]
        sample = {'image': image, 'diagnosis': diagnosis, 'filename': img_name}

        if self.transform:
            image = self.transform(image)
        else:
            raise Exception("Mooney - image not transformed to tensor - transform does not exist")

        # return sample
        assert type(image) == torch.Tensor, "Type of image is " + str(type(image))
        return image, torch.tensor(self.class_map[str(diagnosis)])
