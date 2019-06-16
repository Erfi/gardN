from time import sleep
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import Adafruit_CharLCD.Adafruit_CharLCD as LCD

class GardN:
	HIGH = GPIO.HIGH
	LOW = GPIO.LOW

	def __init__(self, pin_mode=GPIO.BCM):
		GPIO.setmode(pin_mode)
		self.initialize_display()

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

	def initialize_display(self):
		self.lcd = LCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)
		self.lcd.clear()
		self.lcd.message('Starting...')
		sleep(2)

	def print_on_display(self, message):
		self.lcd.clear()
		self.lcd.message(message)

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
			garden.print_on_display(f'Temperature: {int(temperature)}\nHumidity:    {int(humidity)}%')

			if humidity>90 or temperature>30:
				print('setting 18 low: Atomizer OFF')
				garden.set_pin(18, garden.LOW)
			else:
				print('setting 18 high: Atomizer ON')
				garden.set_pin(18, garden.HIGH)
			sleep(5)

	except Exception as ex:
		print(f'**** ERROR ****\n{ex}')

	finally:
		garden.cleanup()
