# Circuit Diagram:
# Components Required: Buzzer -1, Resistance 47K – 1, Reed Switch – 1
# Program:

# Raspberry Pi Connect 

# import RPi.GPIO as GPIO
# import time

# Setup Part
import GPIO as GPIO

reed = 18
# send_capture_signal = 22
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(reed, GPIO.IN)
# GPIO.setup(send_capture_signal, GPIO.OUT)
# Infinite Loop
try:
    while True:
        # Check if Reed Sensor Pin is Lowx
        reed
        _state = GPIO.input(reed)
        if reed _state == False
        print('Now door is open..')
        GPIO.output(buz, True)  # Switch on buzzer
    else:
        # Reed switch is closed so stop buzzer
        GPIO.output(buz, False)
        time.sleep(0.5)  # Wait for half a second before next check

except KeyboardInterrupt:
    print ("CTRL + C Pressed")
    GPIO.output(buz, False)
# Switch of the buzzer
# GPIO.cleanup()
# Clean up and release all GPIO Pins
