# 1D_random_velocity_accelerate-
For study 1D velocity accelerate object sample in Flappy bird's game.


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


## Result ##

![100 steps](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/Figure_14.png?raw=true "100 steps")

![1000 steps](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/Figure_23.png?raw=true "1000 steps")

![2500 steps](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/Figure_25.png?raw=true "2500 steps")

![GIF Flappy birds](https://github.com/jkaewprateep/1D_random_velocity_accelerate-/blob/main/FlappyBirds.gif?raw=true "GIF Flappy birds")
