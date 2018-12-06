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
	h = 1200
	while True:
		sleep(0.01)
		current = motion.get_gravity()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**3))//1
		#print(newMotion)
		x = newMotion[0]+500
		y = newMotion[1]+500
		z = newMotion[2]+1000
		goalX = w/2
		goalY = h/2
		canvas.set_size(w, h)
		canvas.set_fill_color(0, 0, 0)
		canvas.fill_ellipse(goalX, goalY, 30, 30)
		if (abs(goalX-x) < 10 and abs(goalY-y) < 10):
			canvas.set_fill_color(0, 1, 0)
			canvas.fill_ellipse(x, y, 30, 30)
		else:
			canvas.set_fill_color(1, 0, 0)
			canvas.fill_ellipse(x, y, 30, 30)

	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
