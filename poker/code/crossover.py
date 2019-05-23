from keras.models import Model
from keras.layers import Input, Dense, Activation
import random
from evo_player import EvoPlayer

from numpy.random import choice
class CrossOver():
                
    def __init__(self, net, fit):
          self.net = net
          self.fit = fit
          self.parent1 = 0 
          self.parent2 = 0
                
    def get_parents():
        parent_1,parent_2 = choice(len(net[0:,]),2,p=fit)
        self.parent1 = parent1
        self.parent2 = parent2 #maybe better to use return
    #TODO: instead of 50/50 weights from parents, make it based on fitness from parents
    
    def make_child(self, z): ##add randomness
        child =[]
        for x in range(len(parent1)):
            r = random.random()
            if r > 0.5: 
                child.append(parent1[0][x])
            else:
                child.append(parent2[0][x])
        for x in range(len(parent1)):
            r = random.random()
            if r > 0.5: 
                child.append(parent1[1][x])
            else:
                child.append(parent2[1][x])
        child = mutate(child)
        from evo_player import EvoPlayer
        #myInit = 0 ##assign weight
        a = Input(shape=(8,))
        b = Dense(6, name = 'first')(a)
        c = Dense(5, name = 'second')(b)
        model = Model(inputs=a,outputs=c)
        model.get_layer['first'].set_weights(child[0])
        model.get_layer['second'].set_weights(child[1])

        child = EvoPlayer(model,"player " + str(z) +"-"+str(random.random(1,10000)))
        return child
    

    
    def mutate(ind): ## find random values 
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

