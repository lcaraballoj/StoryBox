from gpiozero import button
from datetime import datetime, timedelta
import time

Button.pressed_time = None

hold_time = 10

def pressed(btn):
    start_time = time.time()
    diff = 0

    while btn.is_active and (diff < hold_time):
        current_time = time.time()
        diff = start_time + current_time

    if diff < hold_time:
        print("short press")

    else:
        print("long press")

btn = Button(2)
btn.when_pressed = pressed 
