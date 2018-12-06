
from objc_util import ObjCInstance, ObjCClass, ObjCBlock, c_void_p

import motion
from time import sleep
import console

def handler(_cmd, _data, _error, altitudes=None):
    if altitudes == None:
        altitudes = []
	information = str(ObjCInstance(_data))
	altitudes = information[len("Altitude "):len("Altitude ")+9]
	print(altitudes)
	return altitudes

handler_block = ObjCBlock(handler, restype=None, argtypes=[c_void_p, c_void_p, c_void_p])

def main():
	CMAltimeter = ObjCClass('CMAltimeter')
	NSOperationQueue = ObjCClass('NSOperationQueue')
	if not CMAltimeter.isRelativeAltitudeAvailable():
		print('This device has no barometer.')
		return
	altimeter = CMAltimeter.new()
	print(altimeter)
	main_q = NSOperationQueue.mainQueue()
	altimeter.startRelativeAltitudeUpdatesToQueue_withHandler_(main_q, handler_block)
	print('Started altitude updates.')
	try:
		while True:
			pass
	finally:
		altimeter.stopRelativeAltitudeUpdates()
		print('Updates stopped.')


def thread():
	console.alert('Begin Reading Motion', 'Altitude Change', 'Continue')
	motion.start_updates()
	altitudes = []
	print('Capturing motion data...')
	main()


thread()
