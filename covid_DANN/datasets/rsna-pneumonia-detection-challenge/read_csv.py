import os

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

res = parse_csv("./stage_2_detailed_class_info.csv")
print(
    res['04c08d05-e5f7-4de3-b0b3-d39b3bb9d113']
)
