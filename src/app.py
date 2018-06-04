import json


class Perceptron:

    def __init__(self):
        self.w1 = 0
        self.w2 = 0
        self.bais = 0
        self.threshold = 0

    def Activation_fuction(self, x1, x2, b):
        a =  self.w1 * x1 + self.w2 * x2 + b * self.bais
        if a > self.threshold:
            return 1
        else
            return -1


def Training():
    # defining neuron
    neuron1 = Perceptron()

    # taking data from the training json file
    with open('trainindata.json') as d:
        t_data = json.load(d)

    # using hebbian learning algorithm
    i = 0
    x2 = t_data["x2"]
    bais = t_data["bais"]
    Y = t_data["tarY"]

    for x1 in t_data["x2"]:
        neuron1.w1 = neuron1.w1 + x1 * Y[i]
        neuron1.w2 = neuron1.w2 + x2[i] * Y[i]
        neuron1.bais = neuron1.bais + Y[i]
        i = i + 1


if __name__ == "__main__":
    Training()
