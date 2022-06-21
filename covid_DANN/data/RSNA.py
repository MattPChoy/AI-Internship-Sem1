from torch.utils.data import SubsetRandomSampler, DataLoader, Dataset
import pandas as pd
from .Loader import Loader
import torch
import numpy as np
import os
import cv2
import pydicom

class RSNADataset(Dataset):
    def load_dicom(filename):
        """
        Static class method used to load .dcm images using PyDiCom.
        Installed v2.3.0 using conda install -c conda-forge pydicom(=2.3.0)

        :str abs_fp:       Absolute filepath to root dataset folder
        :str (name):       Optional parameter. If name = None, load all images in folder
                               and return as a list.
                           Else, just load and return that single image
        """
        # Load single image
        dicom_image = pydicom.read_file(filename)
        return dicom_image.pixel_array

    def parse_csv(fp, sep=","):
        """
        Parse a two-column CSV into a key-pair dictionary.
        """
        header = -1
        data = dict()
        print(f"Opening CSV file {fp}")
        with open(fp, "r") as csv_file:
            if header == -1:
                header = [h.strip() for h in csv_file.readline().split(sep)]
            lineNumber = 0
            for line in csv_file:
                if line == '':
                    # At eof
                    break
                if len(line) <= 2:
                    print(f"Line {lineNumber} too short: {str(line)}")
                line = [part.strip() for part in line.split(sep)[:2]]
                data[line[0]] = line[1]
                lineNumber += 1
        return data

    def __init__(self, csv_file, root_dir, transform=None):
        self.source_file = csv_file # For debugging
        self.transform = transform
        self.metadata = pd.read_csv(csv_file)
        self.map = RSNADataset.parse_csv(csv_file)
        self.filenames = sorted(self.map.keys()) # To ensure consistent ordering, only compute once.

        self.root_dir = root_dir
        self.classes = self.metadata['class'].unique()
        self.class_map = {name : idx for idx, name in enumerate(self.classes)}

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        print("Getting from file " + str(self.source_file))
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = self.filenames[idx]
        img_fp = self.root_dir + "\\" + img_name
        if img_name.endswith((".dcm", ".dicom")):
            image = RSNADataset.load_dicom(img_fp)
            image = cv2.resize(image, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
        else:
            image = cv2.imread(img_fp)
            image = cv2.resize(image, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
        # diagnosis = self.metadata.iloc[idx, 1:][0]
        diagnosis = self.map[img_name]
        sample = {'image': image, 'diagnosis': diagnosis, 'filename': img_name}

        if self.transform:
            image = self.transform(image)
        else:
            raise Exception("RSNA - image not transformed to tensor - transform does not exist")

        # return sample
        assert type(image) == torch.Tensor, "Type of image is " + str(type(image))
        return image, torch.tensor(self.class_map[str(diagnosis)])
