import RPi.GPIO as GPIO

class Atomizer:

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)
		GPIO.output(self.pin, GPIO.LOW)

	def turn_on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def turn_off(self):
		GPIO.output(self.pin, GPIO.LOW)

