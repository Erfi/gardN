import Adafruit_DHT as DHT
import logging
from time import sleep


class DHT_sensor:

	def __init__(self, pin, sensor_type=DHT.DHT22):
		self.sensor_type = sensor_type
		self.pin = pin

	def read_sensor_data(self):
		# humidity, temperature = DHT.read_retry(self.sensor_type, self.pin)
		# humidity = int(humidity) if isinstance(humidity, float) else -1
		# temperature = int(temperature) if isinstance(temperature, float) else -1
		logging.info('starting to read sensor')
		sleep(4)
		humidity = 90
		temperature = 15
		logging.info('finishing sensor reading')
		return humidity, temperature


