import motion
import location
from time import sleep

def compass():
	motion.start_updates()
	while True:
		sleep(0.5)
		current = motion.get_magnetic_field()
		newMotion = [0,0,0,0]
		for i in range(len(current)):
			newMotion[i] = (current[i]*(10**2))//1
		print(newMotion)
	motion.stop_updates()

compass()
