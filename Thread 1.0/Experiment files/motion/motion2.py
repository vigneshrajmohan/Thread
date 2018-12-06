import motion
from time import sleep
import console


def main():
	console.alert('Motion Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	motion.start_updates()
	sleep(0.2)
	print('Capturing motion data...')
	while True:
		sleep(0.05)
		current = motion.get_gravity()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**2))//1
		x = newMotion[0]+100
		y = newMotion[1]+100
		z = newMotion[2]+100
		print(x,y,z)
	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
