# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:57:41 2019

@author: Casper
"""

import random
import numpy as np
from pypokerengine.api.game import setup_config, start_poker
from evo_player import EvoPlayer
from crossover import CrossOver

class GameRoom():

    def __init__(self, algorithms, generations):
        self.algorithms = np.array(algorithms)
        self.generations = generations
        indices = np.arange(len(algorithms))
        np.random.shuffle(indices)
        print(indices)
        print(self.algorithms)
        self.algs_random = self.algorithms[indices]
        self.players = makeFirstPlayers()

    def makeFirstPlayers(self):
        players = []
        for x in range(len(self.algs_random)):
            players.append(EvoPlayer(self.algs_random[x],"player "+ str(x))
       return players
                           
    def makeNextPlayers(self, old, new, generation):
       nextGen = []
       while(len(nextGen) < (new/2)):
                           nextGen.append(choice(old,1,p=0.5)) #maybe different p
       nets = []
       fitness = []
       for player in self.players:
                           nets.append(player.get_w())
                           fitness.append(player.get_fitness())
       children = []
       for x in range(new):
                           co = CrossOver(nets,fitness)
                           children.append(co.make_child())
       denominator = 0
       while(len(nextGen) < new):
                           child = choice(children,1,p=0.5)
                           myInit = ##assign weight
                           a = Input(shape=(8,))
                           b = Dense(6, name = 'first', kernel_initializer = myInit)(a)
                           c = Dense(5, name = 'second', kernel_initializer = myInit)(b)
                           model = Model(inputs=a,outputs=c)
                           nextGen.append(EvoPlayer(model, "player " + str(generation) +"-"+str(denominator))
                           denominator += 1
       self.players = nextGen
            
    def start(self):
        for x in range(len(self.algs_random)):
            #table is empty:
            if(x%4 == 0):
                config = setup_config(max_round=100, initial_stack=200, small_blind_amount=10)
            config.register_player(name="player " + str(x),algorithm = self.players[x])
                           
            #table is full:
            if(x%4 == 3):
                game_result = start_poker(config, verbose=1)
                print(game_result)
        game_result = start_poker(config, verbose=1)
                           ##NEED TO EXTRACT WINNING PLAYER AND UPDATE WIN/LOSS OF EVERY PLAYER
  def next(self):
      for x in range(len(self.algs_random)):
          #table is empty:
          if(x%4 == 0):
              config = setup_config(max_round=100, initial_stack=200, small_blind_amount=10)
              config.register_player(name="player " + str(x),algorithm = self.players[x])
              
          #table is full:
          if(x%4 == 3):
              game_result = start_poker(config, verbose=1)
              print(game_result)
      game_result = start_poker(config, verbose=1)
      ##NEED TO EXTRACT WINNING PLAYER AND UPDATE WIN/LOSS OF EVERY PLAYER
                                          
   def doIt(self):
       start()
       for x in range(generations):
                           makeNextPlayers()
                           next()
                           
            
                  ##PLOT TOEVOEGEN
       
