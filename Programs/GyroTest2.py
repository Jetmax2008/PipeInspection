import csv
import time
import board
import busio
import math
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
 
i2c = busio.I2C(board.SCL, board.SDA)
 
sensor = LSM6DS33(i2c)


Time = 0
GyroX = sensor.gyro[0]
GyroY = sensor.gyro[1]
GyroZ = sensor.gyro[2]
pi = math.pi
#Remove Below when 9dof_calibration.py is implemented
#change Below values to the final X,Y,Z Gyro calibration values after running 9dof_calibration.py 
gyro_calibration = [0.06085744935547728, -0.08254316531150682, 0.01488984018107662]

fieldnames = ["Time", "X", "Y", "Z"]

with open('GyroData.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
    with open('GyroData.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        info = {
            "Time": Time,
            "X": GyroX,
            "Y": GyroY,
            "Z": GyroZ,
        }
        
        csv_writer.writerow(info)
        print(Time, GyroX, GyroY, GyroZ)
        
        Time += 1
        GyroX = ((sensor.gyro[0] - gyro_calibration[0])*180)/pi
        GyroY = ((sensor.gyro[1] - gyro_calibration[1])*180)/pi
        GyroZ = ((sensor.gyro[2] - gyro_calibration[2])*180)/pi
        
    time.sleep(1)