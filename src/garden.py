from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
from dht_sensor import DHT_sensor
from display import Display
from atomizer import Atomizer
from project_paths import LOG_PATH



class GardN:
	HIGH = GPIO.HIGH
	LOW = GPIO.LOW

	def __init__(self, atomizer_pin, dht_pin, display_settings):
		GPIO.setmode(GPIO.BCM)
		self.atomizer = Atomizer(pin=atomizer_pin)
		self.dht = DHT_sensor(pin=dht_pin)
		self.display = Display(**display_settings)

	def log(self, message):
		with open(LOG_PATH / 'log.txt', 'a') as fp:
			fp.write(f'{message}\n')

	def cleanup(self):
		GPIO.cleanup()


if __name__ == "__main__":
	try:
		garden = GardN(atomizer_pin=23,
						dht_pin=17,
						display_settings={'rs':26, 'en':19, 'd4':13, 'd5':6, 'd6':5, 'd7':11, 'cols':16, 'lines':2})

		while True:
			humidity, temperature = garden.dht.read_sensor_data()
			garden.log(f'{datetime.now()} | Temperature: {temperature} Humidity:    {humidity}%')
			garden.display.show(f'Temperature: {temperature}\nHumidity:    {humidity}%')

			if humidity>97 or temperature>30:
				garden.log('--- Atomizer OFF ---')
				garden.atomizer.turn_off()
			else:
				garden.log('--- Atomizer ON ---')
				garden.atomizer.turn_on()
			sleep(5)
	except Exception as ex:
		garden.log(str(ex))

	finally:
		garden.cleanup()
