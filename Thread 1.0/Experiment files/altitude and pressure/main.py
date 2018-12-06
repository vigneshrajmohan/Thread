import motion
from time import sleep
import console

from objc_util import ObjCInstance, ObjCClass, ObjCBlock, c_void_p

def get_pressure(tester):

	def handler(_cmd, _data, _error):
		altitude = ObjCInstance(_data).pressure()
		handle_new_data(altitude)

	handler_block = ObjCBlock(handler, restype=None, argtypes=[c_void_p, c_void_p, c_void_p])

	CMAltimeter = ObjCClass('CMAltimeter')
	NSOperationQueue = ObjCClass('NSOperationQueue')
	if not CMAltimeter.isRelativeAltitudeAvailable():
		print('This device has no barometer.')
		return
	altimeter = CMAltimeter.new()
	main_q = NSOperationQueue.mainQueue()
	altimeter.startRelativeAltitudeUpdatesToQueue_withHandler_(main_q, handler_block)
	#print('Started altitude updates.')
	try:
		# while pressure is None:
		# 	pass
		while True:
			tester()
	finally:
		altimeter.stopRelativeAltitudeUpdates()
		#print('Updates stopped.')
		# return pressure


altitudes = []

def handle_new_data(altitude):
	# print(type(altitude))
	# print(altitude.__dict__)
	altitudes.append(altitude)
	print(altitude, altitudes)

# def thread():
# 	return get_pressure()
#
#
# def timedPrint():
# 	while True:
# 		sleep(0.2)
# 		print(thread())
#
# timedPrint()

def get_hyped():
	sleep(0.1)
	print("So hype!")


get_pressure(get_hyped)
