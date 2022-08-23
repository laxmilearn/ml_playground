import numpy as pkg_num
import pathlib as pkg_pathlib

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

play_pathlib_path()
