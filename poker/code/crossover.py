from keras.models import Model
from keras.layers import Input, Dense, Activation
import random
from evo_player import EvoPlayer
import numpy as np
from numpy.random import choice
class CrossOver():
                
<<<<<<< HEAD
    def __init__(self, net = 0, fit = 0, biases = [[0,0,0,0,0,0],[0,0,0]]):
=======
    def __init__(self, net, fit, biases):
          # initializing crossover object, saving parameters
>>>>>>> 2db0fdf4aeda0f4a5127edc0f01574f2ae17b553
          self.net = np.array(net)
          normFit = fit/(np.sum(fit))
          self.fit = normFit
          self.biases = biases
          self.parent1 = 0 
          self.parent2 = 0
                
    def get_parents(self):
        # get parents
        parent_1,parent_2 = choice(self.net.shape[0],2,p=self.fit,replace =False)
        self.parent1 = parent_1
        self.parent2 = parent_2
<<<<<<< HEAD
    
    def make_mutated_child(self, z):
        child = [] #empty new offspring
        self.get_parents()
        temp_1=self.mutate(temp_1)
        temp_2=self.mutate(temp_2)
        from evo_player import EvoPlayer
        a = Input(shape=(8,))
        b = Dense(6, name = 'first')(a)
        c = Dense(3, name = 'second')(b)
        model = Model(inputs=a,outputs=c)
        
        model.get_layer('first').set_weights((np.array(temp_1),np.array(self.biases[0][0])))
        model.get_layer('second').set_weights((np.array(temp_2),np.array(self.biases[0][1])))
        #create new child, with a name tag corresponding to the current generation z
        child = EvoPlayer(model,"player " + str(z) +"-"+str(1000*random.random()))
        
    def make_child(self, z):
=======

    def make_child(self, z): 
        # create crossovers from parents and mutate child
>>>>>>> 2db0fdf4aeda0f4a5127edc0f01574f2ae17b553
        child = []
        self.get_parents()
        temp_1 = []
        for x in range(len(self.net[0][0])):
            temp1 = []
            for y in range(len(self.net[0][0][x])):
                r=random.random()
                if r > 0.5:
                    temp1.append(self.net[self.parent1][0][x][y])
                    #child.append(self.net[self.parent1][x])
                    #child.append(self.biases[self.parent1][x])
                else:
                    temp1.append(self.net[self.parent2][0][x][y])
            temp_1.append(temp1)
        temp_2 = []
        for x in range(len(self.net[0][1])):
            temp2 =[]
            for y in range(len(self.net[0][1][x])):
                r=random.random()
                if r > 0.5:
                    temp2.append(self.net[self.parent1][1][x][y])
                        #child.append(self.net[self.parent1][x])
                        #child.append(self.biases[self.parent1][x])
                else:
                    temp2.append(self.net[self.parent2][1][x][y])
            temp_2.append(temp2)
        temp_1=self.mutate(temp_1)
        temp_2=self.mutate(temp_2)
        from evo_player import EvoPlayer
        a = Input(shape=(8,))
        b = Dense(6, name = 'first')(a)
        c = Dense(3, name = 'second')(b)
        model = Model(inputs=a,outputs=c)

        model.get_layer('first').set_weights((np.array(temp_1),np.array(self.biases[0][0])))
        model.get_layer('second').set_weights((np.array(temp_2),np.array(self.biases[0][1])))
        #create new child, with a name tag corresponding to the current generation z
        child = EvoPlayer(model,"player " + str(z) +"-"+str(1000*random.random()))
        return child
    

    
    def mutate(self,ind):
        # mutate the list of values depending on a factor of its own value.
        for x in range(len(ind)):
            for gene in range(len(ind[0])):
                r = random.random()
                if r < 0.1:
                    # print(ind[x][gene])
                    if r < 0.05:
                        ind[x][gene] = ind[x][gene] *0.9
                    else:
                        ind[x][gene] = ind[x][gene] *1.1
            #currently we do not crossover or mutate biases.
        return ind

    def third_mutate(self,ind):
        j =[] #new layer 1
        for i in ind.get_w():
            for x in range(len(i)):
                for gene in range(len(i[x])):
                    r = random.random()
                    # print(ind[x][gene])
                    if r < 0.5:
                        print("down")
                        i[x][gene] = i[x][gene] *0.9
                    else:
                        print("up")

                        i[x][gene] = i[x][gene] *1.1
            j.append(i)
        from evo_player import EvoPlayer

        a = Input(shape=(8,))
        b = Dense(6, name = 'first')(a)
        c = Dense(3, name = 'second')(b)
        model = Model(inputs=a, outputs=c)
        model.get_layer('first').set_weights((j[0],np.array(self.biases[0])))
        model.get_layer('second').set_weights((j[1],np.array(self.biases[1])))
        #create new child, with a name tag corresponding to the current generation z
        child = EvoPlayer(model,"player " +"-"+str(1000*random.random()))
        return child
