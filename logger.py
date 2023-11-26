import serial
import csv
from time import time
from datetime import datetime


#Open a csv file and set it up to receive comma delimited input
file_name = datetime.now().strftime("%m-%d-%Y_%H-%M-%S") + '_log.csv'
logging = open(file_name, mode='w', newline='')
writer = csv.writer(logging, delimiter=",", escapechar=' ', quoting=csv.QUOTE_NONE)

ser = serial.Serial('COM22', baudrate=115200)
#ser.flushInput()


time_start = time()
elapsed_time_s = 0
time_limit_s = 25
print(f'Logging start, logging for {time_limit_s} sec')

while (elapsed_time_s < time_limit_s):

    #Read in data from Serial until \n (new line) received
    ser_bytes = ser.readline()
    
    #Convert received bytes to text format
    decoded_bytes = (ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    
    #Write received data to CSV file
    writer.writerow([decoded_bytes])

    elapsed_time_s = time() - time_start
            
# Close port and CSV file to exit
ser.close()
logging.close()
print("Logging finished")