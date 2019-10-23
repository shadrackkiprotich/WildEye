from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import serial

port = "/dev/ttyACM0"#put your port here
baudrate = 9600
ser = serial.Serial(port, baudrate)
pir = MotionSensor(4)
val = "llama" # take user input

def tell(msg):
    msg = msg + '\n'
    x = msg.encode('ascii') # encode n send
    ser.write(x)

def hear():
    msg = ser.read_until() # read until a new line
    mystring = msg.decode('ascii')  # decode n return 
    return mystring

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
    tell(val) # send it to arduino
    var = hear() # listen to arduino
    print(var) #print what arduino sent
     
    pir.wait_for_no_motion()
    print("Motion stopped")
