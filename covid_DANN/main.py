import torch
import train
import model
from utils import get_free_gpu
from loaders import source_train_loader, source_test_loader, target_train_loader, target_test_loader
import params

save_name = 'omg'

def main():
    if torch.cuda.is_available():
        get_free_gpu()
        print('Running GPU : {}'.format(torch.cuda.current_device()))
        encoder = model.Extractor().cuda()
        classifier = model.Classifier().cuda()
        discriminator = model.Discriminator().cuda()

        train.source_only(encoder, classifier, source_train_loader, target_train_loader, save_name)
        train.dann(encoder, classifier, discriminator, source_train_loader, target_train_loader, save_name)

    else:
        print("There is no GPU -_-!")


if __name__ == "__main__":
    main()
