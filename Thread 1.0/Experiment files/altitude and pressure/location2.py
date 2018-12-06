# import location
# address_dict = {'Street': 'Infinite Loop', 'City': 'Cupertino', 'Country': 'USA'}
# results = location.geocode(address_dict)
# print (results)
# coordinates = {'latitude': 37.331684, 'longitude': -122.030758}
# results = location.reverse_geocode(coordinates)
# print (results)


import location
from time import sleep
import console

#program spits out the lat and long of my current location
def main():
	console.alert('Motion Experiment 2', 'yo gang gang, we gonna measure this motion', 'Continue')
	location.start_updates()
	sleep(0.2)
	print('Capturing location data...')
	current = location.get_location()
	alt = current['altitude']
	print(alt)
	while True:
		sleep(1)
		current = location.get_location()
		alt = current['altitude']
		print(alt)
	location.stop_updates()
	print('Capture finished, plotting...')



if __name__ == '__main__':
	main()
