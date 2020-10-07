import time
import csv

def saveToCSV(name,BPM_result,IBI_result,SDNN_result,SDSD_result,RMSD_result):
    
    #Open the csv file
    with open (name, mode='a', newline='') as data_file:
                data_writer = csv.writer(data_file, delimiter=',')
                
                # Insert title of the two collumns in the csv file
                #data_writer.writerow(["BPM","IBI","SDNN","RMSD","Etat"])
                
                # Insert in the csv file the value of the metrics
                data_writer.writerow([BPM_result,IBI_result,SDNN_result,SDSD_result,RMSD_result,"SPORT"])
        