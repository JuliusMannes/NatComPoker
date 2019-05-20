from crossover import CrossOver
from keras.models import Model
import numpy as np
from keras.layers import Input, Dense, Activation
import random

fit = np.array([0.1,0.15,0.25,0.5])

net = np.array([1,2,3,4])
net1 = np.array([5,6,7,8])
net2 = np.array([8,9,11,2])
net3 = np.array([6,3,1,9])

net4 = np.array([net,net1,net2,net3])

print(net4)
print(len(net4))
print(len(fit))
parent_1,parent_2 = choice(len(net4[0:,]),2,p=fit)

#parent1 = net4[parent1]
#parent2 = net4[parent2]
print(parent1)
print(parent2)
child =[]
for x in range(len(parent1)):
    r = random.random()
    if r > 0.5: 
        child.append(parent1[x])
    else:
        child.append(parent2[x])

print(child)
for x in range(len(child)):
    r = random.random()
    if r < 0.1:
        if r < 0.05:
            child[x] = child[x] *0.9
        else:
            child[x] = child[x]*1.1
print(child)