from sx1262 import SX1262
import time
from L76 import l76x
import math
import hashlib
from L76.micropyGPS.micropyGPS import MicropyGPS


UARTx = 0
BAUDRATE = 9600
gnss_l76b=l76x.L76X(uartx=UARTx,_baudrate = BAUDRATE)

gnss_l76b.l76x_exit_backup_mode()

# enable/disable sync PPS when NMEA output
'''
optional:
SET_SYNC_PPS_NMEA_ON
SET_SYNC_PPS_NMEA_OFF
'''
gnss_l76b.l76x_send_command(gnss_l76b.SET_SYNC_PPS_NMEA_ON)


# make an object of NMEA0183 sentence parser
"""
Setup GPS Object Status Flags, Internal Data Registers, etc
local_offset (int): Timzone Difference to UTC
location_formatting (str): Style For Presenting Longitude/Latitude:
                           Decimal Degree Minute (ddm) - 40° 26.767′ N
                           Degrees Minutes Seconds (dms) - 40° 26′ 46″ N
                           Decimal Degrees (dd) - 40.446° N
"""
parser = MicropyGPS(location_formatting='dd')

sentence = ''


sx = SX1262(spi_bus=1, clk=10, mosi=11, miso=12, cs=3, irq=20, rst=15, gpio=2)

# LoRa
sx.begin(freq=868, bw=125.0, sf=12, cr=8, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

# FSK
##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
##            tcxoVoltage=1.6, useRegulatorLDO=False,
##            blocking=True)


while True:
    
    if gnss_l76b.uart_any():
        sentence = parser.update(chr(gnss_l76b.uart_receive_byte()[0]))
        if sentence:
            
            #print('WGS84 Coordinate:Latitude(%c),Longitude(%c) %.9f,%.9f'%(parser.latitude[1],parser.longitude[1],parser.latitude[0],parser.longitude[0]))
            data = f'{(parser.latitude[1])},{(parser.longitude[1])},{(parser.latitude[0])},{(parser.longitude[0])},{(parser.altitude)},{(parser.hdop)},{(parser.satellites_in_use)}'

            print(data)

            #gnss_l76b.wgs84_to_bd09(parser.longitude[0],parser.latitude[0])
            #print('Baidu Coordinate: longitude(%c),latitudes(%c) %.9f,%.9f'%(parser.longitude[1],parser.latitude[1],gnss_l76b.Lon_Baidu,gnss_l76b.Lat_Baidu))
            #print('copy Baidu Coordinate and paste it on the baidu map web https://api.map.baidu.com/lbsapi/getpoint/index.html')
            
            #print('UTC Timestamp:%d:%d:%d'%(parser.timestamp[0],parser.timestamp[1],parser.timestamp[2]))
            
#           print fix status
            '''
            1 : NO FIX
            2 : FIX 2D
            3 : FIX_3D
            '''
            print('Fix Status:', parser.fix_stat)
            
            print('Altitude:%d m'%(parser.altitude))
            print('Height Above Geoid:', parser.geoid_height)
            print('Horizontal Dilution of Precision:', parser.hdop)
            print('Satellites in Use by Receiver:', parser.satellites_in_use)
            time.sleep(2)

            data_to_send = data.encode('ascii')
            sx.send(data_to_send)
            time.sleep(2)
    
    
    else:
        sx.send("CANNOT GET GNSS SIGNAL")
        print("CANNOT GET GNSS SIGNAL")
