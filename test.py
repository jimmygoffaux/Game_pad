import RPi.GPIO as GPIO
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as KeyboardController, Key
import time
from datetime import datetime

#with open("/home/tester/Desktop/log.txt", "a") as log:
#    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#    log.write(f"{current_time} - Script start\n")

# Configuration des GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
gpio_pins = [4, 5, 6, 12, 13, 16, 18, 19, 20, 21, 23, 26]
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mouse = Controller()
keyboard = KeyboardController()

def read_gpio_and_move_mouse():
    left_button_pressed = False
    while True:
        if GPIO.input(19) == GPIO.LOW:
            mouse.move(4, 0)  # Déplacer la souris vers la droite
            print("right mouse")
        if GPIO.input(13) == GPIO.LOW:
            mouse.move(-4, 0)  # Déplacer la souris vers la gauche
            print("left mouse")
        if GPIO.input(6) == GPIO.LOW:
            mouse.move(0, 4)  # Déplacer la souris vers le bas
            print("down mouse")
        if GPIO.input(5) == GPIO.LOW:
            mouse.move(0, -4)  # Déplacer la souris vers le haut
            print("up mouse")
        if GPIO.input(23) == GPIO.LOW:
            if not left_button_pressed:
                mouse.press(Button.left)
                left_button_pressed = True
                print("left button pressed")
        else:
            if left_button_pressed:
                mouse.release(Button.left)
                left_button_pressed = False
                print("left button released")

        time.sleep(0.01)  

def gpio21_callback(channel):
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print("enter")

def gpio4_callback(channel):
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    print("esc")

#def gpio23_callback(channel):
#    mouse.click(Button.left)
#    print("left click")

def gpio18_callback(channel):
    mouse.click(Button.right)
    print("right click")

def gpio20_callback(channel):
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    print("left")

def gpio26_callback(channel):
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    print("right")

def gpio16_callback(channel):
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    print("up")

def gpio12_callback(channel):
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    print("down")

GPIO.add_event_detect(21, GPIO.FALLING, callback=gpio21_callback, bouncetime=200)
GPIO.add_event_detect(4, GPIO.FALLING, callback=gpio4_callback, bouncetime=200)
GPIO.add_event_detect(18, GPIO.FALLING, callback=gpio18_callback, bouncetime=200)
#GPIO.add_event_detect(23, GPIO.FALLING, callback=gpio23_callback, bouncetime=200)
GPIO.add_event_detect(20, GPIO.FALLING, callback=gpio20_callback, bouncetime=200)
GPIO.add_event_detect(26, GPIO.FALLING, callback=gpio26_callback, bouncetime=200)
GPIO.add_event_detect(16, GPIO.FALLING, callback=gpio16_callback, bouncetime=200)
GPIO.add_event_detect(12, GPIO.FALLING, callback=gpio12_callback, bouncetime=200)
        

if __name__ == '__main__':
    while True:
        read_gpio_and_move_mouse()
