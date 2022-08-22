import numpy as pkg_num

nda = pkg_num.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(nda.itemsize)
for i in range(nda.ndim):
    print("Dimension = {}, Count = {}".format(i, nda.shape[i]))
