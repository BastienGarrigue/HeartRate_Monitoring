import time
import csv
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import matplotlib.pyplot as plt
i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)
i=0
amplitude=[]
time_signal=[]
temps_actuel=time.time()
while time.time()-temps_actuel<30:
    tension=chan0.value
    amplitude.append(tension)
    time_signal.append(time.time()-temps_actuel)
    with open ('dataRepos.csv', mode='a', newline='') as data_file:
            data_writer = csv.writer(data_file, delimiter=',')
            data_writer.writerow([amplitude[i],time_signal[i]])
    i=i+1
    
plt.plot(amplitude)
plt.show(amplitude)