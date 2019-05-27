from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate
from pypokerengine.engine.hand_evaluator import HandEvaluator
from keras.models import Model
from keras.layers import Input, Dense
import numpy as np
import random

NB_SIMULATION = 1000
#input indices :

def street_to_int(street):
    if(street == 'flop'):
        return 1
    if(street == 'turn'):
        return 2
    if(street == 'river'):
        return 3
    else:
        return 0

class EvoPlayer(BasePokerPlayer):

    def __init__(self, neuralnet, name):
        self.name = name
        self.model = neuralnet
        self.games_played = 0
        self.games_won = 0
        neuralnet.summary()
        self.hole_card = []
        self.all_cards = []
        self.inputs = np.random.random((1, 8))
        # money in pot, street, #player number, dealer button, small blind pos, big blind pos, round count, small blind amount, cardvalue
    def get_name(self):
        return self.name
        
    def add_game_win(self):
        self.games_played += 1
        self.games_won += 1
        print("ADD WIN")
    
    def add_game_lose(self):
        self.games_played += 1

    def get_fitness(self):
        print("won", self.games_won)
        print("total", self.games_played)
        return self.games_won/self.games_played
    
    def get_bias(self):
        first = self.model.get_layer('first').get_weights()[1]
        second = self.model.get_layer('second').get_weights()[1]
        return (first, second)

    def get_w(self):
        first = self.model.get_layer('first').get_weights()[0]
        second = self.model.get_layer('second').get_weights()[0]
        print("SHAPE", self.model.get_layer('second').get_weights()[0].shape)
        print("SECOND", second)
        return (first, second)
    
    def declare_action(self, valid_actions, hole_card, round_state):
        #print(valid_actions)
        #print(self.inputs.shape)
        print("pot: ", round_state['pot'])
        print("sb: ",round_state['small_blind_pos'])
        print("bb: ",round_state['big_blind_pos'])
        community_card = round_state['community_card']
        self.inputs[0][7] = estimate_hole_card_win_rate(nb_simulation=NB_SIMULATION,
                                               nb_player=int(self.inputs[0][2]),
                                               hole_card=gen_cards(hole_card),
                                               community_card=gen_cards(community_card)
                                               )
          
        predictions = self.model.predict(self.inputs)
        choice = np.argmax(predictions[0])
 
        action = valid_actions[choice]
        
        #print(action['action'])
        #print(action['amount'])
        if action['action'] == "raise":
            #action['amount'] = (action['amount']['max'] - action['amount']['min'])*random.random() + action['amount']['min']
            action['amount'] = action['amount']['max']
        
      
        return action['action'], action['amount']

    def receive_game_start_message(self, game_info):
        self.inputs[0][2] = game_info['player_num']
            # for keys,values in game_info.items():
            #print(keys)
            #print(values)
    
    def receive_round_start_message(self, round_count, hole_card, seats):
        self.hole_card = []
        self.hole_card = hole_card
        self.all_cards = []
        pass
    
    def receive_street_start_message(self, street, round_state):
        self.inputs[0][0] = round_state['pot']['main']['amount']
        self.inputs[0][1] = street_to_int(round_state['street'])

        self.inputs[0][3] = round_state['dealer_btn']
        self.inputs[0][4] = round_state['small_blind_pos']
        self.inputs[0][5] = round_state['big_blind_pos']
        self.inputs[0][6] = round_state['round_count']
        pass
    
    def receive_game_update_message(self, action, round_state):
        pass
    
    def receive_round_result_message(self, winners, hand_info, round_state):
        pass


