import os

cwd = os.getcwd()
os.chdir(cwd)
dataDir = "./data"

datasets = [ds for ds in os.listdir(dataDir) if os.path.isdir(os.path.join(cwd, dataDir, ds))]
