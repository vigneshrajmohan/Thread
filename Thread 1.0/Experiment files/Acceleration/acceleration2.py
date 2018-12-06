
import motion
from time import sleep
import console


def main():
	console.alert('Magentic Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	motion.start_updates()
	sleep(0.2)
	print('Capturing motion data...')
	x = 0
	y = 0
	z = 0
	while True:
		sleep(0.2)
		current = motion.get_user_acceleration()
		newMotion = [0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**2))//1
	#if abs(newMotion[0]) > 1:
		x += newMotion[0]
	#if abs(newMotion[1]) > 1:
		y += newMotion[1]
	#if abs(newMotion[2]) > 1:
		z += newMotion[2]
		print(x,y,z)
	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
