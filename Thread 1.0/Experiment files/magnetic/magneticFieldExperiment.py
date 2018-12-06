import motion
from time import sleep
import console


def main():
	console.alert('Magentic Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	motion.start_updates()
	sleep(0.2)
	print('Capturing motion data...')
	while True:
		sleep(0.05)
		current = motion.get_magnetic_field()
		newMotion = [0,0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]//1)
		x = newMotion[0]
		y = newMotion[1]
		z = newMotion[2]
		a = newMotion[3]
		print("X:" + str(x), "Y:" + str(y),"Z:" + str(z), "Acc:" + str(a))
	motion.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
