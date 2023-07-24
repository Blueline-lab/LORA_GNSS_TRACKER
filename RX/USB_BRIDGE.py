from db import Geodata_plotting
from time import sleep
Listen = Geodata_plotting()
from random import uniform

usb = "/dev/ttyACM0"    #Pico USB connection could be ttyACM1 or other name device
table = True
last_value = ""


while True:
    with open(usb, "r") as file :
        recp = file.readline()
        delim = ","
        value = recp.split(delim)

        if table:
            Listen.db_if_table_exist()
            table = False
        
        if last_value != value and value[2] != '0.0':
           Listen.db_write_data(value[2], value[3], value[4])
           
        else: print("NO SIGNAL")
        
        last_value = value
        value = ""

    
