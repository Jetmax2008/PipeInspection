import csv
import time
import board
import busio
import math
import adafruit_lis3mdl

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_lis3mdl.LIS3MDL(i2c)

Time = 0
MagX = sensor.magnetic[0]
MagY = sensor.magnetic[1]
Mag = 0
heading = 0
pi = math.pi
#Remove below when 9dof_calibration.py is implemented
#change Below values to the final X,Y Magnetometer calibration values after running 9dof_calibration.py
mag_calibration =(-55.641625255773164, 15.010230926629646)

fieldnames = ["Time", "MagX", "MagY", "Mag"]

with open('MagData.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    
while True:
    
    with open('MagData.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        info = {
            "Time": Time,
            "MagX": MagX,
            "MagY": MagY,
            "Mag": Mag,
        }
        
        csv_writer.writerow(info)
        print(Time, MagX, MagY, Mag)
        
        Time += 1
        MagX = -sensor.magnetic[0] + mag_calibration[0]
        MagY = sensor.magnetic[1] - mag_calibration[1]
        heading = (math.atan2(MagX,MagY)*180)/pi
        
        if heading < 0:
            Mag = 360 + heading
        else:
            Mag = heading
        
    time.sleep(0.5)