from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from fold_man import FoldMan
from honest_player import HonestPlayer
from console_player import ConsolePlayer
from random_player import RandomPlayer
from evo_player import EvoPlayer

print("hello world")

config = setup_config(max_round=5, initial_stack=1000, small_blind_amount=20)
config.register_player(name="e1", algorithm=HonestPlayer())
config.register_player(name="f2", algorithm=FoldMan())
config.register_player(name="f3", algorithm=FishPlayer())
config.register_player(name="f4", algorithm=FishPlayer())
config.register_player(name="e8", algorithm=HonestPlayer())
config.register_player(name="h1", algorithm=FishPlayer())
config.register_player(name="r2", algorithm=RandomPlayer())
config.register_player(name="e2", algorithm=RandomPlayer())
config.register_player(name="r4", algorithm=RandomPlayer())
config.register_player(name="r5", algorithm=EvoPlayer())
game_result = start_poker(config, verbose=1)
