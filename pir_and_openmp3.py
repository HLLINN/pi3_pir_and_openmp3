import os                                  # for opening mp3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
led = 17
pir = 27
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pir,GPIO.IN)
moved = 0

try:
	while True :
		sleep(0.1)
		moved = GPIO.input(pir)
		if moved ==1:
			GPIO.output(led, True)
			print("Someone moved! Someone moved!")
			action = "mplayer /home/pi/Music/welcome2.mp3"  # file name, for opening mp3 
			os.system(action)                                   # for opening mp3
		else:
			print("No one moved!")
			GPIO.output(led, False)
			sleep(0.5)
finally:
	print("Exit the program")
	GPIO.cleanup()
