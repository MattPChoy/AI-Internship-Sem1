"""
In creating the metadata files, we want to add the following columns:
 -> Filename - all of the files in ./train or ./test
 -> class    - lookup of filename in stage_2_detailed_class_info.csv
"""

import os
import pandas as pd

def get_dirs(fp):
    return [fn for fn in os.listdir(fp) if os.path.isdir(fp + "\\" + fn)]

def get_files(fp):
    return [fn for fn in os.listdir(fp) if os.path.isfile(fp + "\\" + fn)]

def parse_csv(fp, sep=","):
    header = -1
    data = dict()
    with open(fp, "r") as csv_file:
        if header == -1:
            header = [h.strip() for h in csv_file.readline().split(sep)]
            print(f"Headers are: {header}")
        for line in csv_file:
            line = [part.strip() for part in line.split(sep)[:2]]
            data[line[0]] = line[1]
    return data

class_info = parse_csv("./stage_2_detailed_class_info.csv")

"""
Since we don't have the classifications for the
"""
filenames = get_files(os.getcwd() + "\\" + 'train')
print(len(filenames))
with open(f"train_metadata.csv", "w") as metadata:
    metadata.write("filename,class\n")

    for file in filenames[:len(filenames)//2]:
        # Look in ./test and ./train
        fn = file.split(".")[0]
        # print(f"File {fn} of class {class_info[fn]}")
        metadata.write(f"{file},{class_info[fn]}\n")

with open(f"test_metadata.csv", "w") as metadata:
    metadata.write("filename,class\n")

    for file in filenames[len(filenames)//2 + 1:]:
        fn = file.split(".")[0]
        metadata.write(f"{file},{class_info[fn]}\n")
