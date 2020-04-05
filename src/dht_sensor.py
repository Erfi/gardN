import Adafruit_DHT as DHT
import logging
from time import sleep


class DHT_sensor:

	def __init__(self, pin, sensor_type=DHT.DHT22):
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
			logging.info('starting to read sensor')
			humidity, temperature = DHT.read_retry(self.sensor_type, self.pin)
			self.humidity = int(humidity) if isinstance(humidity, float) else -1
			self.temperature = int(temperature) if isinstance(temperature, float) else -1
			logging.info(f'Humidity: {self.humidity} | Temperature: {self.temperature}')
			logging.info('finishing sensor reading')
			sleep(wait)


