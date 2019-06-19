import Adafruit_DHT as DHT

class DHT_sensor:

	def __init__(self, pin, sensor_type=DHT.DHT22):
		self.sensor_type = sensor_type
		self.pin = pin

	def read_sensor_data(self):
		humidity, temperature = DHT.read_retry(self.sensor_type, self.pin)
		humidity = int(humidity) if isinstance(humidity, float) else -1
		temperature = int(temperature) if isinstance(temperature, float) else -1
		return humidity, temperature


