from datetime import datetime, timedelta

Button.pressed_time = None

def pressed(btn):
    if btn.pressed_time:
        if btn.pressed_time + timedelta(seconds = 0.5) > datetime.now():
            print ("Pressed twice")

        else:
            print("Too slow")
        btn.pressed_time = None

btn = Button(10)
btn.when_pressed = pressed
