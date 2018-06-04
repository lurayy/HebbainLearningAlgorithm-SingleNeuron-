import json

class perceptron:

    def __init__(self):
        self.ndata = {
            'w1': 0,
            'w2': 0,
            'b' : 0,
            'threshold' : 0
        }

    def n_fuction(self, x1 ,x2 ,b):
        atf = self.ndata['w1'] * x1 + self.ndata['w2'] * x2 + b * self.ndata['b']
        if atf > self.ndata['threshold']:
            return 1
        else:
            return -1

def training(neuron1):
    with open('trainindata.json') as d:
        t_data = json.load(d)

    i=0
    x1 = t_data['x1']
    x2 = t_data['x2']
    b = t_data['bais']
    for y in t_data['tarY']:
        neuron1.ndata['w1'] = neuron1.ndata['w1'] + x1[i] * y
        neuron1.ndata['w2'] = neuron1.ndata['w2'] + x2[i] * y
        neuron1.ndata['b'] = neuron1.ndata['b'] + y
        i = i + 1

def test(xt1 , xt2, tb):
    return neuron1.n_fuction(xt1 , xt2 , tb)



if __name__ == "__main__":
    neuron1 = perceptron()
    training(neuron1)
    print("Enter input x1 and x2:")
    ix1 = int(input())
    ix2 = int(input())
    tb = 1
    print(test(ix1 , ix2, tb))