#!/usr/bin/python3

import stepper
import RPi.GPIO as GPIO
from PIL import Image
import numpy as np
from gpiozero import Servo
from gpiozero import LED
from time import sleep
import PCF8591 as ADC

global minval
global maxval
minval = 10000
maxval = 0

global servo
servo = Servo(18)

global led
led = LED(26)

global pr
pr = ADC.PCF8591(0x48)

def probe(n,channel):

        sum = 0

        for i in range(n):

                sum += pr.read(channel)

        return sum/n

def stepservo(val):

        servo.value = val
        sleep(0.5)


def scanline(page_width):

        servo.value = -1
        sleep(2)

        global minval
        global maxval

        line = []

        stepsize = 0.2
        scansteps = int(3.14/page_width*2/stepsize)

        led.on()

        for i in range(scansteps):

                val = -1+i*stepsize

                probeval = probe(100,0)
                stepservo(val)

                line.append(probeval)
                if probeval <= minval: minval = probeval
                if probeval >= maxval: maxval = probeval


        led.off()

        #print(line)
        return line


def scan(page_width, page_length):

        lines = []

        for i in range(page_length):

                line = scanline(page_width)
                lines.append(line)

                stepper.Stepper.goAngle(20)

        return lines


def image_conversion(lines):

        lines = np.array(lines)
        lines = (((lines-minval)/maxval)*254)+1
        lines = np.array(lines,dtype=np.uint8)

        image = Image.fromarray(lines)
        return image


def main():

        page_width = 3
        page_length = 2


        lines = scan(page_width, page_length)
        image = image_conversion(lines)
        image.save('scan.jpg')


main()