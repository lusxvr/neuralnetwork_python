import load_mnist
import network

training_data, validation_data, test_data = load_mnist.load_data_wrapper()
training_data = list(training_data)

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)