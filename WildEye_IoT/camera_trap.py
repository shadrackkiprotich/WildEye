from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

PIR_input = 29				#read PIR Output
LED = 32				#LED for signalling motion detected	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)	
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

def trap():
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/tmp/picture.jpg') #save the captured image in this folder
    camera.stop_preview()   

while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        GPIO.output(LED, GPIO.HIGH)
        trap()
    else:
        GPIO.output(LED, GPIO.LOW)
