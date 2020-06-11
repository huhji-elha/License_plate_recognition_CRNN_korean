# train에서 test로 데이터 분할

import shutil
import random
import os
import numpy as np

path = "./DB/train/"
file_list = os.listdir(path)

test_list=[]
test_list = np.random.choice(file_list, 2000, replace=False)
print("tl : {}".format(len(test_list)))
print("fl : {}".format(len(file_list)))

test_path = "./DB/test/"
for i in range(len(test_list)) :
    shutil.move(path + test_list[i], test_path + test_list[i])

file_list = os.listdir(path)
print("after_tl : {}".format(len(test_list)))
print("after_fl : {}".format(len(file_list)))
