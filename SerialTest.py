import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)  

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print(data)

        if data == "1":
            ser.write(b"Y")
