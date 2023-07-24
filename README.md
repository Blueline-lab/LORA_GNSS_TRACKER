# LORA_GNSS_TRACKER
A tracker based on GNSS localisation and transmitting the data by LORA communication


Material used :

    Receiver  :
    - Raspberry Pi 3B
    - Raspberry Pico
    - Pico-LoRa-SX1262 (https://www.waveshare.com/wiki/Pico-LoRa-SX1262)
    Optionnal :
    - Li-ion battery charger regulator
    - SSD for Raspberry Pi 3B

<img src="IMG_9836.jpg" alt="Alt text" title="Optional title">

    

    Transmitter :
    - Raspberry Pico
    - L76B GNSS Module for Raspberry Pi Pico (L76B GNSS Module for Raspberry Pi Pico)
    - Pico-LoRa-SX1262 (https://www.waveshare.com/wiki/Pico-LoRa-SX1262)
    - 3.3v Li-ion battery

<img src="IMG_9841.jpg" alt="Alt text" title="Optional title">

    Map on receiver local network :
    - Install docker & docker-compose on the Raspberry Pi3B Receiver
    - Run "cd /RX && sudo docker-compose up"
    - Run " cd /RX && sudo python3 USB_BRIDGE.py"
    - Get your Receiver IP address and type it on your browser on port 5000
    
        ex : "http://192.168.1.5:5000"
<img src="map.png" alt="Alt text" title="Optional title">
        
