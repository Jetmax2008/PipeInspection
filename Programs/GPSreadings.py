#https://www.youtube.com/watch?v=A1zmhxcUOxw
#Don't Use gpsmon to test gps use cgps -c
#pip3 install gps
import gps
import sys

i = 0
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

sys.stdout = open("location.txt", "w")
print("Latitude, Longitude:")
 
while i == 0:
    try:
        report = session.next()

        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                print(report.lat)
                print(report.lon)
                i = 1
    except KeyboardInterrupt:
        quit()