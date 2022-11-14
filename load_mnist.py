#Libraries
import pickle
import gzip

import numpy as np
import matplotlib.pyplot as plt

def load_data():
    f = gzip.open('data/mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
    f.close
    return(training_data, validation_data, test_data)

#Loading the Dataset
training_data, validation_data, test_data = load_data()

#Plotting the Size of the vectors
print('training_data: ' + str(training_data))
print('validation_data: ' + str(validation_data))
print('test_data: ' + str(test_data))

image_show = 1

print("Digit:")
print(training_data[1][image_show])
plt.matshow(training_data[0][image_show].reshape((28,28)))
plt.show()