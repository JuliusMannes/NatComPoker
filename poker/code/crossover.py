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
        print(self.fit)
        parent_1,parent_2 = choice(self.net.shape[0],2,p=self.fit,replace =False)
        self.parent1 = parent_1
        self.parent2 = parent_2
        print("PARENT1: ", self.parent1)#maybe better to use return
        print("PARENT2: ", self.parent2)#maybe better to use return

    #TODO: instead of 50/50 weights from parents, make it based on fitness from parents

    def make_child(self, z): ##add randomness
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
        #myInit = 0 ##assign weight
        a = Input(shape=(8,))
        b = Dense(6, name = 'first')(a)
        c = Dense(3, name = 'second')(b)
        model = Model(inputs=a,outputs=c)
        print(child[0])
        print(child[1])
        print(child[2])
        print(child[3])
        model.get_layer('first').set_weights((child[0],child[1]))
        model.get_layer('second').set_weights((child[2],child[3]))

        child = EvoPlayer(model,"player " + str(z) +"-"+str(1000*random.random()))
        return child
    

    
    def mutate(self,ind): ## find random values
        for x in range(len(ind)):
            r = random.random()
            if r < 0.1:
                if r < 0.05:
                    ind[x] = ind[x] *0.9
                else:
                    ind[x] = ind[x]*1.1
        return ind        


    def print_status():
        # open a (new) file to write
        outF = open("myOutFile.txt", "w")
        for line in range(len(net)):
            # write weights to output file
            outF.write("writing weights no: " , line)
            outF.write("\n")
            outF.write(net[line])
            outF.write("\n")
        for line in range(len(fit)):
            # write fitnesses to output file
            outF.write("writing fitness no: " , line)
            outF.write("\n")
            outF.write(fit[line])
            outF.write("\n")
            outF.write("parent1:")
            outF.write("\n")
            outF.write(self.parent1)
            outF.write("\n")
            outF.write("parent2:")
            outF.write("\n")
            outF.write(self.parent2)
            outF.write("\n")
            outF.close()

