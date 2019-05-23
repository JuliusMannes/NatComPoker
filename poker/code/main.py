from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from console_player import ConsolePlayer
from random_player import RandomPlayer
from evo_player import EvoPlayer
from game_room import GameRoom

from keras.models import Model
from keras.layers import Input, Dense

print("hello world")

models = []
for x in range(8):
    a = Input(shape=(8,))
    b = Dense(6, name = 'first')(a)
    c = Dense(5, name = 'second')(b)
    models.append(Model(inputs=a, outputs=c))

game_room = GameRoom(models, generations)
game_room.start()

#config.register_player(name="f2", algorithm=FishPlayer())
#config.register_player(name="f3", algorithm=FishPlayer())
#config.register_player(name="f4", algorithm=FishPlayer())
#config.register_player(name="f5", algorithm=FishPlayer())
#config.register_player(name="r1", algorithm=RandomPlayer())
#config.register_player(name="r2", algorithm=RandomPlayer())
#config.register_player(name="r3", algorithm=RandomPlayer())
#config.register_player(name="r4", algorithm=RandomPlayer())
#config.register_player(name="r5", algorithm=RandomPlayer())
#game_result = start_poker(config, verbose=1)
