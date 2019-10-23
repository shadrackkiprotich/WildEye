from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
import serial

import keras
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import decode_predictions
import numpy as np

port = "/dev/ttyACM0"#put your port here
baudrate = 9600
ser = serial.Serial(port, baudrate)
pir = MotionSensor(4)
val = "llama" # take user input
img_path = ""

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
    img_path="/home/pi/smart_cam/image.jpg"
    camera.capture(img_path)
    camera.stop_preview()
    analyse_image()
    send_to_sigfox()

def analyse_image():
    model=load_model("WildEye_AI/Model/wild_eye_v1'h5")
    img=image.load_img(img_path,target_size=(224,224))
    x = image.img_to_array(img)
    x=np.expand_dims(x,axis=0)

    features = model.predict(x)
    print(decode_predictions(features, top=1))
    val = features[0]

def send_to_sigfox():
        tell(val) # send it to arduino
        var = hear() # listen to arduino
        print(var) #print what arduino sent

while True:
    pir.wait_for_motion()
    print("Motion detected")
    trap()     
    pir.wait_for_no_motion()
    print("Motion stopped")
