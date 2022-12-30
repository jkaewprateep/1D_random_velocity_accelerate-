"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PY GAME

https://pygame-learning-environment.readthedocs.io/en/latest/user/games/flappybird.html

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os
from os.path import exists

import tensorflow as tf

import ple
from ple import PLE

from ple.games.flappybird import FlappyBird as flappybird_game
from ple.games import base
from pygame.constants import K_w, K_h

import matplotlib.pyplot as plt

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
None
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
config = tf.config.experimental.set_memory_growth(physical_devices[0], True)
print(physical_devices)
print(config)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Variables
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
nb_frames = 100000000000
step = 0
gamescores = 0.0
reward = 0.0

pipe_gap = 250

actions = { "up___1": K_w, "none_1": K_h }

list_X = [ ]
list_Y = [ ]
list_Distance = [ ]
list_Velocity = [ ]
list_Acceleration = [ ]

list_X.append( 0 )
list_Y.append( 512 / 2 )
list_Distance.append( 0 )
list_Velocity.append( 0 )
list_Acceleration.append( 0 )

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Functions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def random_action(  ): 
	rewards = 0.0
	
	gameState = p.getGameState()
	player_y_array = gameState['player_y']
	player_vel_array = gameState['player_vel']
	next_pipe_dist_to_player_array = gameState['next_pipe_dist_to_player']
	next_pipe_top_y_array = gameState['next_pipe_top_y']
	next_pipe_bottom_y_array = gameState['next_pipe_bottom_y']
	next_next_pipe_dist_to_player_array = gameState['next_next_pipe_dist_to_player']
	next_next_pipe_top_y_array = gameState['next_next_pipe_top_y']
	next_next_pipe_bottom_y_array = gameState['next_next_pipe_bottom_y']
	
	gap = (( next_pipe_bottom_y_array - next_pipe_top_y_array ) / 2 )
	top = next_pipe_top_y_array
	target = top + gap
	
	space = 512 - pipe_gap 
	upper_pipe_buttom = next_pipe_top_y_array + 0.8 * space
	
	coeff_01 = upper_pipe_buttom
	coeff_02 = 512 - player_y_array
	
	temp = tf.random.normal([2], 0.001, 0.5, tf.float32)
	temp = tf.ones([2], tf.float32)
	temp = tf.math.multiply(temp, tf.constant([ coeff_01, coeff_02 ], shape=(2, 1), dtype=tf.float32))
	# temp = tf.nn.softmax(temp)
	# 
	
	temp = tf.math.argmax(temp)
	action = int(temp[0])
	
	action_name = list(actions.values())[action]
	action_name = [ x for ( x, y ) in actions.items() if y == action_name]
	
	print( "steps: " + str( step ).zfill(6) + " action: " + str(action_name) + " coeff_01: " + str(int(coeff_01)).zfill(6) + " coeff_02: " + str(int(coeff_02)).zfill(6) 

	)

	return action

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
: Environment
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
game_console = flappybird_game(width=288, height=512, pipe_gap=pipe_gap)
p = PLE(game_console, fps=30, display_screen=True)
p.init()

obs = p.getScreenRGB()

for i in range(nb_frames):
	
	step = step + 1
	gamescores = gamescores + reward
	reward = 0
	
	#############################################
	gameState = p.getGameState()
	player_y_array = gameState['player_y']
	player_vel_array = gameState['player_vel']
	
	list_X.append( step )
	list_Y.append( player_y_array )
	list_Distance.append( pow( pow( list_X[ step - 1] - list_X[ step ], 2 ) + pow( list_Y[ step - 1 ] - list_Y[ step ], 2 ), 0.5 ) )
	list_Velocity.append( player_vel_array )
	list_Acceleration.append( abs( list_X[ step - 1] - list_X[ step ] ) * abs(player_vel_array) )
	#############################################
	
	if p.game_over():	
		step = 0
		gamescores = 0
		reward = 0	
		
		game_console = flappybird_game(width=288, height=512, pipe_gap=250)
		p = PLE(game_console, fps=30, display_screen=True)
		p.init()
		p.reset_game()
		
		list_X = [ ]
		list_Y = [ ]
		list_Distance = [ ]
		list_Velocity = [ ]
		list_Acceleration = [ ]
		
		list_X.append( 0 )
		list_Y.append( 512 / 2 )
		list_Distance.append( 0 )
		list_Velocity.append( 0 )
		list_Acceleration.append( 0 )
		
	if ( step == 0 ):
		print('start .... ' )
		
		for j in range(8):
			reward = p.act(K_h)
			reward = p.act(K_w)
		
		for j in range(15):
			reward = p.act(K_h)
			reward = p.act(K_h)
			
		for j in range(3):
			reward = p.act(K_h)
			reward = p.act(K_w)
	
	else :
		action = random_action( )
		reward = p.act(list(actions.values())[action])
		input('...')
		
	if ( step % 100 == 0 ):
		plt.plot(list_X, list_Y, linewidth=2.0,  color='green')
		plt.plot(list_X, list_Distance, linewidth=2.0,  color='red')
		plt.plot(list_X, list_Velocity, linewidth=2.0,  color='blue')
		plt.plot(list_X, list_Acceleration, linewidth=2.0,  color='yellow')
		plt.title("Flappy Birds flying distance")
		plt.xlabel("Distance as length: step = " + str( step ) )
		# plt.ylabel("Distance as height")
		plt.legend(['Distance as height', 'Relative Distance', 'Velocity', 'Acceleration'])
		plt.show()
		
input('END !!!')
