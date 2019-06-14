import RPi.GPIO as GPIO
import time

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

	def cleanup(self):
		GPIO.cleanup()


if __name__ == "__main__":
	try:
		garden = GardN()
		garden.setup_output(18)

		for i in range(5):
			print(f'High')
			garden.set_pin(18, garden.HIGH)
			time.sleep(1)
			print(f'Low')
			garden.set_pin(18, garden.LOW)
			time.sleep(1)


	except Exception as ex:
		print(f'**** ERROR ****\n{ex}')

	finally:
		garden.cleanup()
