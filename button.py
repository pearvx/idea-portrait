import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
#GPIO.setup(24, GPIO.OUT)  #LED to GPIO24


def button_pressed():
    print('hello!')
    try:
        while True:
             button_one_state = GPIO.input(23)
             button_two_state = GPIO.input(4)
             button_three_state = GPIO.input(3)
             if button_one_state == False:
                 #GPIO.output(24, True)
                 print('fine Button Pressed...')
                 time.sleep(0.2)
                 return 0

             elif button_two_state == False:
                 #GPIO.output(24, True)
                 print('depends Button Pressed...')
                 time.sleep(0.2)
                 return 1
             elif button_three_state == False:
                 #GPIO.output(24, True)
                 print('worried Button Pressed...')
                 time.sleep(0.2)
                 return 2
             #else:
                 #GPIO.output(24, False)
    except:
        GPIO.cleanup()
