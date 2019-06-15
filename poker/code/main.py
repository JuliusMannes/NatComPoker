from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from honest_player import HonestPlayer
from console_player import ConsolePlayer
from random_player import RandomPlayer
from evo_player import EvoPlayer
from game_room import GameRoom
from keras.models import model_from_json

from keras.models import Model
from keras.layers import Input, Dense

import timeit

start = timeit.timeit()
print ("hello")

models = []
for x in range(8):
    a = Input(shape=(8,))
    b = Dense(6, name = 'first')(a)
    c = Dense(3, name = 'second')(b)
    models.append(Model(inputs=a, outputs=c))
# load json and create model
#json_file = open('badass.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#m = model_from_json(loaded_model_json)
generations = 10
amount_per_generation = 10

game_room = GameRoom(models, generations, amount_per_generation)
game_room.train_generations()
end = timeit.timeit()
outTime = open("Time.txt", "w")
outTime.write("Time elapsed: %d" %(end-start))
outTime.write("\n")
print (end - start)
outTime.close()

##THIS IS JUST FOR TESTING
#config = setup_config(max_round=50, initial_stack=1000, small_blind_amount=10)
#config.register_player(name="f2", algorithm=HonestPlayer())
#config.register_player(name="f3", algorithm=HonestPlayer())
#config.register_player(name="f4", algorithm=HonestPlayer())
#config.register_player(name=e.get_name(),algorithm = e)
#config.register_player(name="r1", algorithm=RandomPlayer())
#config.register_player(name="r2", algorithm=RandomPlayer())
#config.register_player(name="r3", algorithm=RandomPlayer())
#config.register_player(name="r4", algorithm=RandomPlayer())
#config.register_player(name="r5", algorithm=RandomPlayer())
#game_result = start_poker(config, verbose=1)
