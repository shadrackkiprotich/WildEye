import serial
port = "/dev/ttyACM0"#put your port here
baudrate = 9600
ser = serial.Serial(port, baudrate)
def tell(msg):
    msg = msg + '\n'
    x = msg.encode('ascii') # encode n send
    ser.write(x)

def hear():
    msg = ser.read_until() # read until a new line
    mystring = msg.decode('ascii')  # decode n return 
    return mystring

while True:
    val = input() # take user input
    tell(val) # send it to arduino
    var = hear() # listen to arduino
    print(var) #print what arduino sent