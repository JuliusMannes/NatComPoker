from keras.models import Model
from keras.layers import Input, Dense, Activation
import random
from evo_player import EvoPlayer
import numpy as np
from numpy.random import choice
class CrossOver():
                
    def __init__(self, net, fit, biases):
          self.net = np.array(net)
          normFit = fit/(np.sum(fit))
          self.fit = normFit
          self.biases = biases
          self.parent1 = 0 
          self.parent2 = 0
                
    def get_parents(self):
        parent_1,parent_2 = choice(self.net.shape[0],2,p=self.fit,replace =False)
        self.parent1 = parent_1
        self.parent2 = parent_2

    def make_child(self, z): 
        child = []
        self.get_parents()
        for x in range(self.net.shape[1]):
            r = random.random()
            if r > 0.5: 
                child.append(self.net[self.parent1][x])
                child.append(self.biases[self.parent1][x])
            else:
                child.append(self.net[self.parent2][x])
                child.append(self.biases[self.parent2][x])
        child = self.mutate(child)
        from evo_player import EvoPlayer
        a = Input(shape=(8,))
        b = Dense(6, name = 'first')(a)
        c = Dense(3, name = 'second')(b)
        model = Model(inputs=a,outputs=c)
        model.get_layer('first').set_weights((child[0],child[1]))
        model.get_layer('second').set_weights((child[2],child[3]))
        #create new child, with a name tag corresponding to the current generation z
        child = EvoPlayer(model,"player " + str(z) +"-"+str(1000*random.random()))
        return child
    

    
    def mutate(self,ind):
        for x in range(len(ind)):
            r = random.random()
            for gene in ind[0]:
                if r < 0.01:
                    if r < 0.005:
                        ind[x] = ind[x] *0.9
                    else:
                        ind[x] = ind[x]*1.1
            for gene in ind[2]:
                if r < 0.01:
                    if r < 0.005:
                        ind[x] = ind[x] *0.9
                    else:
                        ind[x] = ind[x]*1.1
            ##indices 0 and 2 are the weights of layer 1 and 2, indices 1 and 3 are biases
            #currently we do not crossover or mutate biases.
        return ind        

