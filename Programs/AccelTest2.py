import csv
import time
import board
import busio
import math
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
 
i2c = busio.I2C(board.SCL, board.SDA)
 
sensor = LSM6DS33(i2c)

Time = 0
AccelX = sensor.acceleration[0]
AccelY = sensor.acceleration[1]
AccelZ = sensor.acceleration[2]
pi = math.pi

fieldnames = ["Time", "AccelX", "AccelY", "AccelZ", "MagX", "MagY", "Mag"]

with open('AccelData.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
    with open('AccelData.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        info = {
            "Time": Time,
            "AccelX": AccelX,
            "AccelY": AccelY,
            "AccelZ": AccelZ,
        }
        
        csv_writer.writerow(info)
        print(Time, AccelX, AccelY, AccelZ)        
        Time += 1
        AccelX = sensor.acceleration[0]
        AccelY = sensor.acceleration[1]
        AccelZ = sensor.acceleration[2]
        
    time.sleep(0.5)