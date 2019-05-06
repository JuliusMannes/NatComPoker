# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:34:21 2019

@author: Casper
"""

from pypokerengine.players import BasePokerPlayer
import random as rand
from keras.models import Model
from keras.layers import Input, Dense

class NeuralNetPlayer(BasePokerPlayer):

  def __init__(self, neuralnetwork):
    self.model = neuralnetwork

  def set_action_ratio(self, fold_ratio, call_ratio, raise_ratio):
    ratio = [fold_ratio, call_ratio, raise_ratio]
    scaled_ratio = [ 1.0 * num / sum(ratio) for num in ratio]
    self.fold_ratio, self.call_ratio, self.raise_ratio = scaled_ratio

  def declare_action(self, valid_actions, hole_card, round_state):
    choice = self.__choice_action(valid_actions)
    action = choice["action"]
    amount = choice["amount"]
    if action == "raise":
      amount = rand.randrange(amount["min"], max(amount["min"], amount["max"]) + 1)
    return action, amount

  def __choice_action(self, valid_actions):
      neuraal netwerk(inputs, inputs)
    r = rand.random()
    if r <= self.fold_ratio:
      return valid_actions[0]
    elif r <= self.call_ratio:
      return valid_actions[1]
    else:
      return valid_actions[2]


  def receive_game_start_message(self, game_info):
      self.game_info = game_info
    pass

  def receive_round_start_message(self, round_count, hole_card, seats):
      
    pass

  def receive_street_start_message(self, street, round_state):
    pass

  def receive_game_update_message(self, new_action, round_state):
    pass

  def receive_round_result_message(self, winners, hand_info, round_state):
    pass

