import serial
ser = serial.Serial('/dev/cu.usbmodemFD121', 9600)
while True:
    print ser.readline()
