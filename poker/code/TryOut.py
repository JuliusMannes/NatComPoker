from crossover import CrossOver
from keras.models import Model
import numpy as np
from keras.layers import Input, Dense, Activation
import random

fit = np.random.uniform(low=0.0,high=1.0,size= (24,0))
net = np.zeros(123)
parent1 = 0
parent2 = 0
cv = 0
fit = np.sort(fit)
r = random.random()
print("r",r)
print("fit",fit)
for x in fit:
    cv = x
    next = fit[x+1] + cv
    print("cv", cv)
    print("next",next)
    
    if r < next and r >cv:  ##potential bug
        parent1 = x+1
r = random.random()
for x in fit:
    if r < x+1 and r >x:  ##potential bug
        parent2 = x+1
