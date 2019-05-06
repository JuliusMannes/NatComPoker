from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate
from keras.models import Model
from keras.layers import Input, Dense

NB_SIMULATION = 1000
inputs = []

class EvoPlayer(BasePokerPlayer):
    
    def _init_(self, weights)
    
    def declare_action(self, valid_actions, hole_card, round_state):


    def receive_game_start_message(self, game_info):
        self.nb_player = game_info['player_num']
    
    def receive_round_start_message(self, round_count, hole_card, seats):
        inputs.append
    
    def receive_street_start_message(self, street, round_state):
        pass
    
    def receive_game_update_message(self, action, round_state):
        pass
    
    def receive_round_result_message(self, winners, hand_info, round_state):
        pass

