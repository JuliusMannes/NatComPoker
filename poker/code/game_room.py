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

    def __init__(self, algorithms, generations, rounds_per_gen):
        self.algorithms = np.array(algorithms)
        self.generations = generations
        self.rounds_per_gen = rounds_per_gen
        self.players = self.init_players()
        self.players = self.shuffle_players()
        
    def shuffle_players(self):
        indices = np.arange(len(self.players))
        np.random.shuffle(indices)
        return np.array(self.players)[indices]

    def init_players(self):
        players = []
        for x in range(len(self.algorithms)):
            players.append(EvoPlayer(self.algorithms[x],"player "+ str(x)))
        return players
                           
    def update_generation(self, mu, z):
       nextGen = []
       ranked_players = sorted(self.players, key=lambda x: x.games_won, reverse=True)
       mu_ranked_players = ranked_players[:mu]
       for p in mu_ranked_players:
           nextGen.append(p)
       #To-do: mutation and crossover
       nets = []
       fitness = []
       for player in mu_ranked_players:
                           nets.append(player.get_w())
                           fitness.append(player.get_fitness())
       children = []
       for x in range(len(self.players) - mu):
                           co = CrossOver(nets,fitness)
                           children.append(co.make_child(z))
       
       for c in children:
           print(c.get_name())
           nextGen.append(c)
           
       self.players = nextGen
            
    #start function
    def play_rounds(self):
        for z in range(self.generations):
            for x in range(self.rounds_per_gen):
                self.players = self.shuffle_players()
                self.play_game()
            print("NEW GENERATION")
            self.update_generation(4, z)

    def find_winner(self, game_result):
        stacks = []
        players = []
        for x in game_result['message']['game_information']['seats']:
            stacks.append((x['stack']))
            idx = stacks.index(max(stacks))
            players.append(x['name'])
        winner = players[idx]
        return winner
            
    def play_game(self):
        tables  =2
        for table in range(tables):
            players = self.players[table*4:4*(table+1)]
            config = setup_config(max_round=1, initial_stack=200, small_blind_amount=10)
            for p in players:
                config.register_player(name=p.get_name(),algorithm = p)
                print("added a player")
            print("play game")
            game_result = start_poker(config, verbose=2)
            winner = self.find_winner(game_result)
            
            for p in players:
                if  p.name == winner:
                    #print("WE ADD A GAME WIN")
                    p.add_game_win()
                else:
                    p.add_game_lose()                                #extract winner:

                      
                           
       
