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
	moalX = w/2 -100
	moalY = h/2 -100
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
		moalX += (x-102)*2
		moalY += (y-102)*2
		if goalX <= 0 or goalY <= 0 or goalX >= w or goalY >= h:
			goalX -= (x-100)
			goalY -= (y-100)
		if moalX <= 0 or moalY <= 0 or moalX >= w or moalY >= h:
			moalX -= (x-102)*2
			moalY -= (y-102)*2
		canvas.set_size(w, h)
		canvas.set_fill_color(0, 0, 0)
		canvas.fill_ellipse(goalX, goalY, 30, 30)
		canvas.set_fill_color(0, 0, 1)
		canvas.fill_ellipse(moalX, moalY, 30, 30)

	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
