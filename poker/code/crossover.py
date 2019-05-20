from keras.models import Model
from keras.layers import Input, Dense, Activation
import random

from numpy.random import choice
class CrossOver():
                
    def __init__(self, net, fit, kids):
          self.net = net
          self.fit = fit
          self.parent1 = 0 
          self.parent2 = 0
          self.kids = kids
                
    def get_parents():
        parent_1,parent_2 = choice(len(net[0:,]),2,p=fit)
        self.parent1 = parent1
        self.parent2 = parent2 #maybe better to use return
    #TODO: instead of 50/50 weights from parents, make it based on fitness from parents
    
    def make_child():
        child =[]
        for x in range(len(parent1)):
            r = random.random()
            if r > 0.5: 
                child.append(parent1[x])
            else:
                child.append(parent2[x])
        return child
    
    
    def make_children():
        children = []
        for x in range(kids):
            children.append(make_child)
        return children
    
    def mutate(ind):
        for x in range(len(ind)):
            r = random.random()
            if r < 0.1:
                if r < 0.05:
                    ind[x] = ind[x] *0.9
                else:
                    ind[x] = ind[x]*1.1
        return ind        