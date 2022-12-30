# 1D_random_velocity_accelerate-
For the study, 1D velocity accelerates object samples in the Flappy bird games.

## Sample single input to output relatioship ##

With a single requirement, we consider it as an action of ```K_w``` for press key W and press nothing as ```K_h```. It is easy as you understand two options on the left and right of ```[ upper_pipe_buttom, 512 - pipe_gap ]``` which side has more value than another will be selected and its index use as an action index to select an action from the action list ```actions = { "up___1": K_w, "none_1": K_h }```

```
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
```

## Sample multiple inputs to output relatioship ##

For some reason, we need to study further about the equation and value response to function or correlated response we need to know about how distances create within the area space and we try to make use of it flying slove if you observed see it differently flying patterns.

```
# safety value
safety_value = 15
	
# Left side point degrades
leftside_velocity_pt = int( next_pipe_dist_to_player_array  / 2 )
	
# right side point degrades
rightside_velocity_pt = int( next_pipe_dist_to_player_array  + ( next_next_pipe_dist_to_player_array - 
             next_pipe_dist_to_player_array ) / 2 )
	
# position Y upper gap
next_pipe_top_y_array

# position Y standard gap
next_pipe_bottom_y_array 

# position Y upper gap next
next_next_pipe_top_y_array

# position Y standard gap next
next_next_pipe_bottom_y_array
	
# distance from player_y_array to upper gap
distance_upper_gap = player_y_array - next_pipe_top_y_array - safety_value

# distance from player_y_array to standard gap
distance_standard_gap = next_pipe_bottom_y_array - player_y_array + safety_value

# distance from player_y_array to upper gap next
distance_upper_gap_next = player_y_array - player_y_array - safety_value

# distance from player_y_array to standard gap next
distance_standard_gap_next = next_next_pipe_bottom_y_array - player_y_array + safety_value

# acceleration
accleration = accum_velocity + distance_upper_gap * accum_velocity
	
contrl = gamescores + ( 50 * reward )
coff_0 = player_y_array
coff_1 = leftside_velocity_pt
coff_2 = rightside_velocity_pt
coff_3 = next_pipe_top_y_array
coff_4 = next_pipe_bottom_y_array
coff_5 = accum_velocity
coff_6 = accleration
coff_7 = distance_upper_gap
coff_8 = distance_standard_gap
coff_9 = next_next_pipe_top_y_array
coff_10 = next_next_pipe_bottom_y_array
coff_11 = distance_upper_gap_next
coff_12 = distance_standard_gap_next
coff_13 = safety_value
coff_14 = step
```

## Files and Directory ##

| File name | Description  |
--- | --- |
| Sample.py | sample random codes for testing with AI |
| Figure_14.png | plottings 100 step runnning |
| Figure_23.png | plottings 1,000 step runnning |
| Figure_25.png | plottings 2,500 step runnning |
| FlappyBirds.gif | GIF animation game play |
| README.md | readme file |

## Result ##

![100 steps](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/Figure_14.png?raw=true "100 steps")

![1000 steps](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/Figure_23.png?raw=true "1000 steps")

![2500 steps](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/Figure_25.png?raw=true "2500 steps")

![GIF Flappy birds](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/FlappyBirds.gif?raw=true "GIF Flappy birds")
