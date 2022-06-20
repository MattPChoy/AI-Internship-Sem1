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

    def __init__(self, csv_file, root_dir, transform=None):
        self.transform = transform
        self.metadata = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.classes = self.metadata['class'].unique()
        self.class_map = {name : idx for idx, name in enumerate(self.classes)}

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir, self.metadata.iloc[idx, 0])
        if img_name.endswith((".dcm", ".dicom")):
            image = RSNADataset.load_dicom(img_name)
            image = cv2.resize(image, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
        else:
            image = cv2.imread(img_name)
            image = cv2.resize(image, dsize=(224,224), interpolation=cv2.INTER_CUBIC)
        diagnosis = self.metadata.iloc[idx, 1:][0]
        sample = {'image': image, 'diagnosis': diagnosis, 'filename': img_name}

        if self.transform:
            image = self.transform(image)
        else:
            raise Exception("RSNA - image not transformed to tensor - transform does not exist")

        # return sample
        assert type(image) == torch.Tensor, "Type of image is " + str(type(image))
        return image, torch.tensor(self.class_map[str(diagnosis)])
