import numpy as pkg_num
import pathlib as pkg_pathlib
import random as pkg_random

def play_numpy_array_shape():
  nda = pkg_num.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
  print(nda.itemsize)
  for i in range(nda.ndim):
    print("Dimension = {}, Count = {}".format(i, nda.shape[i]))

def play_pathlib_path():
  temp_dirpath = pkg_pathlib.Path.cwd()
  temp_filepath = temp_dirpath.joinpath("sample_file.txt")
  print("File: Name = {}, Stem = {}, Extension = {}".format(
    temp_filepath.name, temp_filepath.stem, temp_filepath.suffix))

def play_dict():
  data_dict = {
    "k1" : "v11", "k2" : "v22", "k3" : "v33", "k4" : "v44", 
    "k5" : "v55", "k6" : "v66", "k7" : "v77", "k8" : "v88" 
  }
  print((type(data_dict), data_dict.__len__()))
  print(data_dict.keys())
  print(data_dict.values())
  data_values = list(data_dict.values())
  print((type(data_values), data_values.__len__()))

  sample_values = pkg_random.sample(data_values, 3)
  print("Sample Values = ", sample_values)

def play_array():
  items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
  sample_items = pkg_random.sample(items, 3)
  print(sample_items)

play_array()
play_dict()
