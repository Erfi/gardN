import Adafruit_CharLCD.Adafruit_CharLCD as LCD
import logging
from time import sleep

class Display(LCD):

	def __init__(self, rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2):
		super().__init__(rs=rs, en=en, d4=d4, d5=d5, d6=d6, d7=d7, cols=cols, lines=lines)
		self.clear()

	def show(self, message):
		logging.info('Starting to display')
		self.clear()
		sleep(3)
		self.message(message)
		logging.info('finishing display')
