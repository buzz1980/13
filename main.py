def on_button_pressed_a():
    global stappen
    stappen = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global stappen
    stappen += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

stappen = 0
stappen = 0

def on_forever():
    basic.show_number(stappen)
basic.forever(on_forever)
