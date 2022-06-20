from data import MooneyDataset, RSNADataset
import cv2
import os

mooney = MooneyDataset(
    csv_file = os.getcwd() + "\\datasets\\mooney\\train_metadata.csv",
    root_dir = os.getcwd() + "\\datasets\\mooney\\images"
)

i = 0
for image, label in mooney:
    cv2.imshow(label, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Label:" + label)

    if i >= 3:
        break
    i += 1

# import loaders
# import cv2
#
# for test_images, test_labels in loaders.source_train_loader:
#     test_image = test_images[0]
#     test_label = test_labels[0]
#     cv2.imshow(test_label, test_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
