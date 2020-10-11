import time
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation
# Import function 
from saveToCSV import saveToCSV
from HRV.metrics import BPM, IBI, SDNN, SDSD, sympatho_vagal_balance
from DataExtraction.getRRListAmp import get_rr_list_amp
from writeData_csv import writeData
from livePlotter import live_plotter
from displaySignal import display
import pickle
from sklearn.ensemble import RandomForestClassifier


def slidingWindowRealTime():
    
    i2c = busio.I2C(board.SCL, board.SDA)

    ads = ADS.ADS1115(i2c)

    chan0 = AnalogIn(ads, ADS.P0)
    chan1 = AnalogIn(ads, ADS.P1)
    chan2 = AnalogIn(ads, ADS.P2)
    chan3 = AnalogIn(ads, ADS.P3)
    
    i=0
    x = []
    y = []
    amplitude=[]
    time_signal=[]
    temps_actuel=time.time()

    # Launch variable
    lancement=True
    
    # Window size
    window_size = 10
    line1=[]
    
    # Starting time of the signal

    x_vec =[0]
    y_vec = [0]
    if lancement == True:
            while time.time()-temps_actuel<window_size:
                tension=chan0.value
                amplitude.append(tension)
                time_signal.append(time.time()-temps_actuel)
            lancement=False
    start_time=time_signal[0]
    time_start_window=time.time()
    while True:
            tension=chan0.value
            amplitude.append(tension)
            time_signal.append(time.time()-temps_actuel)
            #end_time = time_signal[-1]
            temps_ecoule=time.time()-time_start_window
            #for i in range(round(start_time), round(end_time)-window_size):
            
            if time.time()-time_start_window>=1:
                time_start_window=time.time()
                time_window_30sec = [t for t in time_signal if i <= t <= i+window_size]
                     
                    # Extract the min and the max of the signal inside the window
                min_time = min(time_window_30sec)
                max_time = max(time_window_30sec)
                
                    # Index of min and max time
                index_min_time = time_window_30sec.index(min_time)
                index_max_time = time_window_30sec.index(max_time)

                    # Amplitude of signal inside window
                amplitude_window_30sec = amplitude[index_min_time:index_max_time]
                
                x = get_rr_list_amp(amplitude_window_30sec,time_window_30sec)
                signal = display(amplitude_window_30sec)
                BPM_result = BPM(x)
                IBI_result = IBI(x)
                SDNN_result = SDNN(x)
                SDSD_result = np.std(SDSD(x))
                RMSSD_result = np.sqrt(np.mean(SDSD(x)))
                X_pred=[[BPM_result,IBI_result,SDNN_result,SDSD_result,RMSSD_result],]
                with open('model.pickle','rb') as modelFile:
                     model = pickle.load(modelFile)
                pred= model.predict(X_pred)
                if pred == [1]:
                    print("L'utilisateur a fait un effort")
                else:
                    print("L'utilisateur est au repos")
                
                if i>20:
                    plt.plot(amplitude)
                    plt.show()
                i=i+1
                
                #start_time=start_time+1
                   
    print("END")
  
slidingWindowRealTime()    