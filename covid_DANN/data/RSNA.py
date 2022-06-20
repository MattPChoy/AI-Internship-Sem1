from torch.utils.data import SubsetRandomSampler, DataLoader, Dataset
import pandas as pd
from .Loader import Loader
import torch
import numpy as np
import os
import cv2

class RSNADataset(Dataset):
    def load_dicom(abs_fp, name=None):
        """
        Static class method used to load .dcm images using PyDiCom.
        Installed v2.3.0 using conda install -c conda-forge pydicom(=2.3.0)

        :str abs_fp:       Absolute filepath to root dataset folder
        :str (name):       Optional parameter. If name = None, load all images in folder
                               and return as a list.
                           Else, just load and return that single image
        """

        if (name != None):
            # Load single image
            dicom_image = pydicom.read_file(abs_fp + "/" + name)
            return dicom_image.pixel_array

        else:
            images = []
            # print(os.listdir(abs_fp))
            filenames = [fn for fn in os.listdir(abs_fp) if fn.endswith(('.dcm', '.dicom'))]
            # print(f"DICOM Filenames: {filenames}")

            for fn in filenames:
                dicom_image = pydicom.read_file(abs_fp + "/" + fn)
                images.append(dicom_image.pixel_array)
            return images

    def __init__(self, csv_file, root_dir, transform=None):
        self.transform = transform
        self.metadata = pd.read_csv(csv_file)
        self.root_dir = root_dir

    def __len__(self):
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
