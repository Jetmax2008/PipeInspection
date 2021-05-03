#sudo apt install python3-gi-cairo
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


def animate(i):
    GyroData = pd.read_csv('GyroData.csv')
    x = GyroData['Time']
    y1 = GyroData['X']
    y2 = GyroData['Y']
    y3 = GyroData['Z']

    plt.cla()

    plt.plot(x, y1, label='X-axis')
    plt.plot(x, y2, label='Y-axis')
    plt.plot(x, y3, label='Z-axis')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()