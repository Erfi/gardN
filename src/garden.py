import random
import logging
import concurrent.futures
import threading
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
from dht_sensor import DHT_sensor
from display import Display
from atomizer import Atomizer
from project_paths import LOG_PATH



class GardN:
    HIGH = GPIO.HIGH
    LOW = GPIO.LOW

    def __init__(self, atomizer_pin, dht_pin, display_settings):
        GPIO.setmode(GPIO.BCM)
        self.cleanup()
        self.atomizer = Atomizer(pin=atomizer_pin)
        self.dht = DHT_sensor(pin=dht_pin)
        self.display = Display(**display_settings) # not used bc RPI cannot provide enough power for all

    def cleanup(self):
        GPIO.cleanup()


if __name__ == "__main__":
    # setup the logger
    logging.basicConfig(filename=str(LOG_PATH / 'log.txt'),
                            filemode='a', 
                            format='%(levelname)s - %(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', 
                            level=logging.INFO)
    
    try:
        logging.info('Initializing')
        garden = GardN(atomizer_pin=23,
                       dht_pin=18,
                       display_settings={'rs':26, 'en':19, 'd4':13, 'd5':6, 'd6':5, 'd7':11, 'cols':16, 'lines':2})
        """ 
        create threads (daemons) for:
        - pulsing the atomizer,
        - reading sensors
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(garden.atomizer.pulse, sec_on=300, sec_off=2400)
            executor.submit(garden.dht.read_sensor_data, wait=300)            

    except Exception as ex:
        logging.error('Exception occurred', exc_info=True)

    finally:
        logging.info('cleaning up')
        garden.cleanup()
