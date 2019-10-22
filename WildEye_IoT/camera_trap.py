from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)

def trap():
    camera = PiCamera()
    camera.start_preview()
    for i in range(5):
        sleep(1)
        camera.capture('/home/pi/smart_cam/image%s.jpg' % i)
        camera.stop_preview()

while True:
    pir.wait_for_motion()
    print("Motion detected")
    trap()
    
    pir.wait_for_no_motion()
    print("Motion stopped")
