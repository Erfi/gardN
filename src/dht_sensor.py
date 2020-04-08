import Adafruit_DHT as DHT
import logging
from time import sleep


class DHT_sensor:

	def __init__(self, pin, sensor_type=DHT.DHT11):
		self.sensor_type = sensor_type
		self.pin = pin
		self.temperature = None
		self.humidity = None

	def read_sensor_data(self, wait):
		"""
		Args:
			wait: seconds to wait until the next reading
		"""
		while True:
			logging.debug('starting to read sensor')
			humidity = None
			temperature = None
			max_tries = 5
			for i in range(max_tries):
				logging.debug(f'sensor reading try {i}')
				humidity, temperature = DHT.read_retry(self.sensor_type, self.pin)
				logging.debug(f'sensor reading after try {i}: Humidity: {humidity} | Temperature: {temperature}')
				if isinstance(humidity, float) and isinstance(temperature, float):
					self.humidity = int(humidity)
					self.temperature = int(temperature)
					break
				else:
					sleep(3)
			else:
				self.humidity = -1
				self.temperature  -1
			logging.info(f'Humidity: {self.humidity} | Temperature: {self.temperature}')
			logging.debug('finishing sensor reading')
			sleep(wait)


