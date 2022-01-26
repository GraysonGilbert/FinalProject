from gpiozero import DistanceSensor
from time import sleep

def detect_page():

        from gpiozero import DistanceSensor
        from time import sleep

        sensor = DistanceSensor(echo=19, trigger=13)

        reading = sensor.distance * 100
        sleep(1)
        print('Distance: ', reading)

        if reading <= 0.25: x = 0
        else: x = 1
        return x
~
