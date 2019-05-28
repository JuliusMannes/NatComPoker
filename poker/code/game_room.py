# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:57:41 2019

@author: Casper
"""
from fish_player import FishPlayer
from console_player import ConsolePlayer
from random_player import RandomPlayer
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
           #print("NEXTGEN PLAYER NAME: " , p.name)
           nextGen.append(p)
       #To-do: mutation and crossover
       nets = []
       fitness = []
       biases = []
       for player in mu_ranked_players:
           # print("Player name:", player.name )
           #print("Player games played :", player.games_played)
           # print("Player games won :", player.games_won)

                           nets.append(player.get_w())
                           biases.append(player.get_bias())
                           fitness.append(player.get_fitness())
       
                           player.games_played = 0   ##reset the score for the new generation
                           player.games_won = 0
       
       children = []
       for x in range(len(self.players) - mu):
                           co = CrossOver(nets,fitness, biases)
                           children.append(co.make_child(z))
       for c in children:
           #print("NEXTGEN CHILD PLAYER NAME: " , c.name)
           nextGen.append(c)
           
       self.players = nextGen
            
    #start function
    def play_rounds(self):
        for z in range(self.generations):
            for x in range(self.rounds_per_gen):
                self.players = self.shuffle_players()
                self.play_game()
            print("NEW GENERATION: " , z)
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
            config = setup_config(max_round=100, initial_stack=2000, small_blind_amount=10)
            for p in players:
                config.register_player(name=p.get_name(),algorithm = p)
            #print("added player: ", p.name)
            print("play game")
            game_result = start_poker(config, verbose=0)
            winner = self.find_winner(game_result)
            
            for p in players:
                if  p.name == winner:
                    #print("WE ADD A GAME WIN to player: ", p.name)
                    p.add_game_win()
                else:
                    #print("We add a game lose: ", p.name)
                    p.add_game_lose()                                #extract winner:

    def save_players(self, players):
        name = "model_x.json"
        weights = "model_x.h5"
        for p in players:
            model_json = p.model.to_json()
            with open(str.replace(name,"x",p.name), "w") as json_file:
                json_file.write(model_json)
            # serialize weights to HDF5
            p.model.save_weights(str.replace(weights,"x",p.name))
            print("Saved model to disk")
    
    def benchmark(self, player, rounds, stage, file): ##gets best player of the last gen for benchmarking
        for x in range(rounds):
            config = setup_config(max_round=100, initial_stack=2000, small_blind_amount=10)
            config.register_player(name=player.get_name(),algorithm = player)
            config.register_player(name="f2", algorithm=RandomPlayer())
            config.register_player(name="f3", algorithm=RandomPlayer())
            config.register_player(name="f4", algorithm=RandomPlayer())
            game_result = start_poker(config, verbose=0)
            winner = self.find_winner(game_result)
            if  player.name == winner:
                #print("WE ADD A GAME WIN to player: ", p.name)
                player.add_game_win()
            else:
            #print("We add a game lose: ", p.name)
                player.add_game_lose()
        wins = player.games_won
        print(player.name, " has won: " , wins)
        file.write("At stage: %d, the player has won: %d " %(stage, wins))
        file.write("\n")


    def train_generations(self):
        outF = open("Benchmark.txt", "w")
        stages = 1
        for x in range(stages):
            self.play_rounds()
            ranked_players = sorted(self.players, key=lambda x: x.games_won, reverse=True)
            self.benchmark(ranked_players[0],100,x,outF)
        self.save_players(self.players)
        #uncomment this if you rly want to save models
        outF.close()

                      
                           
       
