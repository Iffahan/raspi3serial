import serial

ser = serial.Serial('/dev/ttyS0', 9600)  # Use the appropriate serial port

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print(data)

        if data == "1":
            ser.write(b"Y")
