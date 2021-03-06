import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [12,16,20,21] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
             [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0  # current position in stator sequence

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir = +/- 1 (ccw / cw)
  global state
  global pins
  global sequence
  state += dir
  if state > 7: state = 0
  elif state < 0: state =  7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1500)

def moveSteps(steps, dir):
  # move the actuation sequence a given number of half steps
  for i in range(steps):
    halfstep(dir)

class Stepper:

  def goAngle(angle):
     angle = int(angle) # Change string to int
     if angle-180 > 0: # Finding which direction is shortest
       angle = 360-angle # Altering angle if direction changes
       dir = -1
     else: dir = 1
     moveSteps(int(angle*4096/360),dir) # Moves angle and direction
