import motion
import matplotlib.pyplot as plt
from time import sleep
import console
import canvas


def main():
	console.alert('Motion Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	motion.start_updates()
	sleep(0.2)
	print('Capturing motion data...')
	w = 512
	h = 512
	while True:
		sleep(0.1)
		current = motion.get_gravity()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**3))//1
		#print(newMotion)
		if newMotion[0] < 1001 and newMotion[0] > 900 and newMotion[1] > -50 and newMotion[1] < 50 and newMotion[2] > -50 and newMotion[2] < 50:
			canvas.set_size(w, h)
			canvas.set_fill_color(1, 0, 0)
			canvas.fill_ellipse(0, 0, w, h)
		if newMotion[0] > -1001 and newMotion[0] < -900 and newMotion[1] > -50 and newMotion[1] < 50 and newMotion[2] > -50 and newMotion[2] < 50:
			canvas.set_size(w, h)
			canvas.set_fill_color(0, 1, 0)
			canvas.fill_ellipse(0, 0, w, h)
		if newMotion[0] > -50 and newMotion[0] < 50 and newMotion[1] > -50 and newMotion[1] < 50 and newMotion[2] > -1001 and newMotion[2] < -900:
			canvas.set_size(w, h)
			canvas.set_fill_color(0, 0, 1)
			canvas.fill_ellipse(0, 0, w, h)
	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
