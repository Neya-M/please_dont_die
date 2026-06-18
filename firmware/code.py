import board
import digitalio
import time
import adafruit_dht

global next_action
next_action = time.time()
global water_off
water_off = time.time()
global fan_off
fan_off = time.time()
global low_batt
low_batt = False
task = 0
placeholder = 0  # this is a placeholder value for temperatures and humidity

valve = digitalio.DigitalInOut(board.GP14)
valve.direction = digitalio.Direction.OUTPUT

LBO = digitalio.DigitalInOut(board.GP0)
LBO.direction = digitalio.Direction.INPUT

fan = digitalio.DigitalInOut(board.GP13)
fan.direction = digitalio.Direction.OUTPUT

therm = digitalio.DigitalInOut(board.A0)
therm.direction = digitalio.Direction.INPUT

dht = adafruit_dht.DHT11(board.GP15)

LED = digitalio.DigitalInOut(board.GP11)
LED.direction = digitalio.Direction.OUTPUT

Button = digitalio.DigitalInOut(board.GP12)
Button.direction = digitalio.Direction.OUTPUT


def schedule(minshours, action):  # see below comment for action numbers
    global next_action
    global water_off
    global fan_off
    if action == 1:
        water_off = time.time() + minshours * 60
    elif action == 2:
        fan_off = time.time() + minshours * 60
    else:
        next_action = time.time() + minshours * 3600


def action(index):  # 0: checks, 1: shut water, 2: shut fan
    global low_batt
    global fan_off
    global water_off
    if LBO.value:
        low_batt = True
    if index == 1:
        valve.value = False
    if index == 2:
        fan.value = False
    else:
        if dht.temperature > 27.0:
            fan.value = True
            schedule(5, 2)
        if dht.humidity < placeholder:
            schedule(10, 1)
        elif dht.humidity > placeholder:
            pass
        else:
            schedule(5, 1)
        schedule(6, 0)


while True:
    if Button.value and low_batt:
        LED.value = True
        time.sleep(1)
        LED.value = False
    now = time.time()
    global next_action
    if now >= water_off:
        action(1)
    if now >= fan_off:
        action(2)
    if now >= next_action:
        action(0)
    time.sleep(1)
