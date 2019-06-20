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
		pulse_count = 0
		while True:
			garden.atomizer.pulse(sec_on=5, sec_off=10)
			pulse_count = pulse_count + 1 if pulse_count <= 5 else 0
			if pulse_count == 5:
				humidity, temperature = garden.dht.read_sensor_data()
				garden.log(f'{datetime.now()} | Temperature: {temperature} Humidity:    {humidity}%')
				garden.display.show(f'Temperature: {temperature}\nHumidity:    {humidity}%')

	except Exception as ex:
		garden.log(str(ex))

	finally:
		garden.log('cleaning up')
		garden.cleanup()
