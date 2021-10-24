import numpy as np
import os

input_folder = "./dataset/images/train/"
train_data = sorted(os.listdir(input_folder))

names=[]
for file_name in train_data:
	if '.jpg' in file_name or '.jpeg' in file_name or '.png' in file_name:
		print(os.path.join("..", input_folder, file_name))
		names.append(os.path.join("..", input_folder, file_name))

np.savetxt(input_folder+"train.txt", np.array(names))