import canvas
import motion
import matplotlib.pyplot as plt
from time import sleep
import console

##Does not work because I am not using animation library

def main():
	console.alert('Motion Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	motion.start_updates()
	sleep(0.2)
	print('Capturing motion data...')
	num_samples = 100
	w = 512
	h = 512
	for nums in range(num_samples):
		canvas.set_size(w, h)
		sleep(0.05)
		current = motion.get_gravity()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**3))//1
		print(newMotion)
		canvas.set_fill_color(1, 0, 0)
		canvas.fill_ellipse(0, 0, newMotion[1], newMotion[2])
	motion.stop_updates()
	print('Capture finished, plotting...')





if __name__ == '__main__':
	main()
