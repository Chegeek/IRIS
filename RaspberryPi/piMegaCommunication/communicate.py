import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)

#wait for mega start up
print('Saying hello')
port.write("H")
print('Sent H')
print('Arduino is reading')

while True:
    ch=port.read()
    if(ch=='A'):
        print('read')
        print(ch)
        print('Sending ACK')
        port.write('A')
        print('Mega is ready')
        break


