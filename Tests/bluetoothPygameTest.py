import serial, time

time.sleep(2)
arduino = serial.Serial("COM4", 9600)
print("Setup complete")
time.sleep(2)
arduino.write(("HI!").encode())
print("Finished")