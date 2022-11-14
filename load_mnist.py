#Importing MNIST
from keras.datasets import mnist

#Loading the Dataset
(train_X, train_y), (test_X, test_y) = mnist.load_data()

#Plotting the Size of the vectors
print('X_train: ' + str(train_X.shape))
print('y_train: ' + str(train_y.shape))
print('X_test: ' + str(test_X.shape))
print('y_test: ' + str(test_y.shape))

print(type(train_X))
print(type(train_y))

print(train_X[0])