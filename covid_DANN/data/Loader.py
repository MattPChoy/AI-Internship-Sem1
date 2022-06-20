"""
This class defines
"""

from torch.utils.data import SubsetRandomSampler, DataLoader
import torchvision.datasets as datasets
from torchvision import transforms
from abc import ABC, abstractmethod

class Loader(ABC):
    def __init__(self, mean, stdev):
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(
                (mean, mean, mean),
                (stdev, stdev, stdev)
            )
        ])

    @abstractmethod
    def get_train(download=True):
        pass

    @abstractmethod
    def get_validate(download=True):
        pass

    @abstractmethod
    def get_test(download=True):
        pass
