import numpy as np

dataset = np.loadtxt('diabetes.csv', delimiter=',', skiprows=1)

dataset_x = dataset[:, :8]
dataset_y = dataset[:, 8]

from sklearn.model_selection import train_test_split

training_dataset_x, test_dataset_x, training_dataset_y, test_dataset_y = train_test_split(dataset_x, dataset_y, train_size=0.8)


 