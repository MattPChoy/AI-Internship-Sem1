"""
For generating a metadata.csv file for the Mooney dataset.
Of structure:
 /data (root)
    /test
        /NORMAL (classes)
        /PNEUMONIA
    /train
        /NORMAL (classes)
        /PNEUMONIA
    /val
        /NORMAL (classes)
        /PNEUMONIA

We want to convert to structure:
{filename}, {diagnosis / class}
"""

import os

sources = ['test', 'train', 'val']

def get_dirs(fp):
    return [fn for fn in os.listdir(fp) if os.path.isdir(fp + "\\" +fn)]

def get_files(fp):
    return [fn for fn in os.listdir(fp) if os.path.isfile(fp + "\\" + fn)]



for src in sources:
    with open(f"{src}_metadata.csv", "w") as metadata_file:
        metadata_file.write("filename,class\n")
        path = os.getcwd() + "\\" + src
        print(f"Searching in {path}")
        # For test, train, validate:
        classes = get_dirs(path)
        print(f"Classes are: {classes}")
        for c in classes:
            print(f"Searching in {path}\\{c}")
            for fn in get_files(path + "\\" + c):
                metadata_file.write(f"{fn},{c}\n")
"""
with open("metadata.csv", "w") as metadata_file:
    # Write the header line
    metadata_file.write("filename, class, source" + os.linesep)
    for src in sources:
        path = os.getcwd() + "\\" + src
        print(f"Searching in {path}")
        # For test, train, validate:
        classes = get_dirs(path)
        print(f"Classes are: {classes}")
        for c in classes:
            print(f"Searching in {path}\\{c}")
            for fn in get_files(path + "\\" + c):
                metadata_file.write(f"{fn}, {c}, {src}" + os.linesep)
"""
