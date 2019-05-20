# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:57:41 2019

@author: Casper
"""

import random
import numpy as np
from pypokerengine.api.game import setup_config, start_poker
from evo_player import EvoPlayer

class GameRoom():

    def __init__(self, algorithms):
        self.algorithms = np.array(algorithms)
        indices = np.arange(len(algorithms))
        np.random.shuffle(indices)
        print(indices)
        print(self.algorithms)
        self.algs_random = self.algorithms[indices]
      
    def start(self):
        for x in range(len(self.algs_random)):
            #table is empty:
            if(x%4 == 0):
                config = setup_config(max_round=100, initial_stack=200, small_blind_amount=10)
            config.register_player(name="player " + str(x), algorithm=EvoPlayer(self.algs_random[x],"player "+ str(x)))
            #table is full:
            if(x%4 == 3):
                game_result = start_poker(config, verbose=1)
                print(game_result)
        game_result = start_poker(config, verbose=1)