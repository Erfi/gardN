from time import sleep
import RPi.GPIO as GPIO
import logging

class Atomizer:

	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.OUT)
		GPIO.output(self.pin, GPIO.LOW)

	def turn_on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def turn_off(self):
		GPIO.output(self.pin, GPIO.LOW)

	def pulse(self, sec_on, sec_off):
		logging.info('starting the pulse')
		self.turn_on()
		sleep(sec_on)
		self.turn_off()
		sleep(sec_off)
		logging.info('ending the pulse')

