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
	goalX = w/2
	goalY = h/2
	locations = []
	while True:
		sleep(0.01)
		current = motion.get_gravity()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**2))//1
		#print(newMotion)
		x = newMotion[0]+100
		y = newMotion[1]+100
		z = newMotion[2]+100
		goalX += (x-100)
		goalY += (y-100)
		if goalX <= 0 or goalY <= 0 or goalX >= w or goalY >= h:
			goalX -= (x-100)
			goalY -= (y-100)
		canvas.set_size(w, h)
		canvas.set_fill_color(0, 0, 0)
		canvas.fill_ellipse(goalX, goalY, 30, 30)
		locations += [goalX]
		locations += [goalY]
		for i in range(0, len(locations)-2, 2):
			canvas.set_fill_color(0, 0, 0)
			canvas.fill_ellipse(locations[i], locations[i+1], 30, 30)



	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
