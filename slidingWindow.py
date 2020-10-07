import time
import csv
import pandas as pd
import numpy as np
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Import function 
from saveToCSV import saveToCSV
from HRV.metrics import BPM, IBI, SDNN, SDSD, sympatho_vagal_balance
from DataExtraction.getRRListAmp import get_rr_list_amp
from writeData_csv import writeData

def slidingWindow():
    
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
    
    # Save the data in two lists
    while time.time()-temps_actuel<60:
        tension=chan0.value
        amplitude.append(tension)
        time_signal.append(time.time()-temps_actuel)
    
    print("while finit")
    # Ending time of the signal
    end_time = time_signal[-1]
    
    # Starting time of the signal
    start_time = time_signal[0]

    # Window size
    window_size = 30

    for i in range(0, round(end_time)-window_size):
        time_window_30sec = [t for t in time_signal if i <= t <= t+30]
        
        # Extract the min and the max of the signal inside the window
        min_time = min(time_window_30sec)
        max_time = max(time_window_30sec)
        
        # Index of min and max time
        index_min_time = time_window_30sec.index(min_time)
        index_max_time = time_window_30sec.index(max_time)
        
        # Amplitude of signal inside window
        amplitude_window_30sec = amplitude[index_min_time:index_max_time]
        
        print("CSV amp,time")
        # Create csv file to save signal (amplitude and time) inside the window

        x = get_rr_list_amp(amplitude_window_30sec,time_window_30sec)
        
        BPM_result = BPM(x)
        IBI_result = IBI(x)
        SDNN_result = SDNN(x)
        SDSD_result = np.std(SDSD(x))
        RMSD_result = np.sqrt(np.mean(SDSD(x)))
        #BalanceSV_result = np.sqrt(np.mean(sympatho_vagal_balance(x)))
        
        # Export data into a CSV file
        print("CSV dataset")
        saveToCSV("TEST_dataset.csv",BPM_result,IBI_result,SDNN_result,SDSD_result,RMSD_result)
        print("END")
        
slidingWindow()