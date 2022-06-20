from data import MooneyDataset, RSNADataset
from torch.utils.data import SubsetRandomSampler, DataLoader, Dataset
import torchvision.transforms as transforms
import os
import params

source_train_dataset = RSNADataset(
    csv_file = os.getcwd()+"\\datasets\\rsna-pneumonia-detection-challenge\\train_metadata.csv",
    root_dir = os.getcwd()+"\\datasets\\rsna-pneumonia-detection-challenge\\train",
    transform = transforms.ToTensor()
)

source_test_dataset = RSNADataset(
    csv_file = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\test_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\rsna-pneumonia-detection-challenge\\train",
    transform = transforms.ToTensor()
)

target_train_dataset = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\mooney\\train_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\mooney\\images",
    transform = transforms.ToTensor()
)

target_test_dataset = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\mooney\\train_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\mooney\\images",
    transform = transforms.ToTensor()
)

source_train_loader = DataLoader(
    source_train_dataset,
    batch_size = params.batch_size,
    sampler = SubsetRandomSampler(range(len(source_train_dataset))),
    num_workers = params.num_workers
)

source_test_loader = DataLoader(
    source_test_dataset,
    batch_size = params.batch_size,
    sampler = SubsetRandomSampler(range(len(source_test_dataset))),
    num_workers = params.num_workers
)

target_train_loader = DataLoader(
    target_train_dataset,
    batch_size = params.batch_size,
    sampler = SubsetRandomSampler(range(len(target_train_dataset))),
    num_workers = params.num_workers
)

target_test_loader = DataLoader(
    target_test_dataset,
    batch_size = params.batch_size,
    sampler = SubsetRandomSampler(range(len(target_test_dataset))),
    num_workers = params.num_workers
)
