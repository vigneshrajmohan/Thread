import motion
from time import sleep
import console
import canvas
import math


def main():
	console.alert('Motion Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	motion.start_updates()
	sleep(0.2)
	print('Capturing motion data...')
	w = 1000
	h = 1400

	while True:
		sleep(0.01)
		canvas.set_size(w, h)
		current = motion.get_gravity()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**3))//1
		#print(newMotion)
		x = newMotion[0]+1000
		y = newMotion[1]+1000
		z = newMotion[2]+1000
		goalX = w/2
		goalY = h/2


		#bottom
		if (z < 1000):
			canvas.set_fill_color(1, 0, 0)
			canvas.draw_text("bottom", x-500, y-400, font_name='Courier New', font_size=50.0)
	#top
		if (z > 1000):
			canvas.set_fill_color(0, 0, 1)
			canvas.draw_text("top", 1500-x, 1700-y, font_name='Courier New', font_size=50.0)
	#right
		canvas.set_fill_color(0, 0, 1)
		canvas.draw_text("right", 500-x, 1500-y, font_name='Courier New', font_size=50.0)
	#left
		canvas.set_fill_color(0, 0, 1)
		canvas.draw_text("left", x-1500, 1500-y, font_name='Courier New', font_size=50.0)
	#front
		canvas.set_fill_color(0, 0, 1)
		canvas.draw_text("front", 500-y, 1500-z, font_name='Courier New', font_size=50.0)
	#back
		canvas.set_fill_color(0, 0, 1)
		canvas.draw_text("back", y-1500, z-500, font_name='Courier New', font_size=50.0)

		# if (z > 1000):
		# 	canvas.set_fill_color(0, 0, 1)
		# 	canvas.draw_text("top", 1500-x, 1700-y, font_name='Courier New', font_size=50.0)

	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
