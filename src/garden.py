from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

class GardN:
	HIGH = GPIO.HIGH
	LOW = GPIO.LOW

	def __init__(self, pin_mode=GPIO.BCM):
		GPIO.setmode(pin_mode)

	def setup_output(self, pin):
		GPIO.setup(pin, GPIO.OUT)

	def setup_input(self, pin):
		GPIO.setup(pin, GPIO.IN)

	def set_pin(self, pin, val):
		GPIO.output(pin, val)

	def get_pin(self, pin):
		return GPIO.input(pin)

	def read_DHT_sensor(self, pin, sensor_type=DHT.DHT11):
		return DHT.read_retry(sensor_type, pin)

	def cleanup(self):
		GPIO.cleanup()


if __name__ == "__main__":
	try:
		print('Starting...')
		garden = GardN()
		garden.setup_output(18)

		while True:
			humidity, temperature = garden.read_DHT_sensor(17)
			print(f'humidity: {humidity} | temperature: {temperature}')

			if humidity > 18:
				print('setting 18 low')
				garden.set_pin(18, garden.LOW)
			else:
				print('setting 18 high')
				garden.set_pin(18, garden.HIGH)
			sleep(1)

	except Exception as ex:
		print(f'**** ERROR ****\n{ex}')

	finally:
		garden.cleanup()
