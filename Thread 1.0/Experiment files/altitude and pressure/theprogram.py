import pressuremeasure

import motion
from time import sleep
import console


def thread():
	console.alert('Begin Reading Motion', 'Altitude Change', 'Continue')
	motion.start_updates()
	altitudes = []
	print('Capturing motion data...')
	main()
	while True:
		sleep(0.2)
		print(pressureRun())
	motion.stop_updates()
	print('Capture finished, plotting...')




thread()
