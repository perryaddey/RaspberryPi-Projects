# LCD Displaying IP Address on Raspberry Pi at Startup 

**This is great for people who are trying to use a Raspberry Pi connected to Wi-Fi with a dynamic IP address!**

As a college student, because I use my university's guest wifi, the only way to ssh into my Pi is to use the IP address (i.e. pi@172.31.81.153). 
Since I'm forced to deal with the dynamic guest wifi IP address, I wrote some code that's super helpful in getting my IP address once I turn the Pi on.


## Instructions

1. Wire your [I2C LCD 1602](https://www.amazon.com/SunFounder-Serial-Module-Display-Arduino/dp/B019K5X53O/ref=sr_1_2?crid=1LZHYTICPA2ZY&dib=eyJ2IjoiMSJ9.y_PDtxm8kl477UgZqriw3b21Hjp2lUOtTe7LGYJZDeZQ-XrH6puWg7rHLvnvW7l5pcalM1G0qjgjk-P842ZyYMiiEUk3FNKcn0GKeoq6rVnBKxN2n6EcWsoIX7R38hHsP1kq83PENUZfQTmdW0vjuuUR3R9qGZfcUTXVoAzNV2AnLsMwjLnTVgMVqLIOVI3grFksgKwi17LeIqAFS98zJJ5x2MMIOnTQ_beKhcjZF7U.qh0NmEVKvwEcUtILmObenkPhzY-26ZAoqxxs1kpAyOs&dib_tag=se&keywords=i2c%2B1602%2Blcd%2Bsunfounder&qid=1732168470&sprefix=i2c%2B1602%2Blcd%2Bsunofunder%2Caps%2C116&sr=8-2&th=1) to your pi (make sure I2C is turned on)
  
2. Using [`LCD1602.py`](https://github.com/sunfounder/SunFounder_SensorKit_for_RPi2/blob/master/Python/LCD1602.py) from Sunfounder, clone my repository
```
git clone https://github.com/perryaddey/RaspberryPi-Projects.git
```
```
cd RaspberryPi-Projects/LCD-IP-Address/
```
3. Run `getipaddress.py` to make sure your IP address is displayed on the LCD (if there is an error, try restarting your pi)
```
python3 getipaddress.py
````   
4. We are using a script to run `getipaddress.py` from startup, so run `pwd` in the current directory and replace line 4 in `launcher.sh` to `cd <output from pwd>`

```
#! /bin/bash

cd /                                 
cd /home/pi/RaspberryPi-Projects/LCD-IP-Address  #example for line 4
python3 getipaddress.py 
cd /
```
6. Make the script executable and run it to check that it works
```
chmod 755 launcher.sh
```
```
sh launcher.sh
```
6. To get launcher.sh to run at pi startup, edit crontab (again, make edits to the path based on where your files are)
```
sudo crontab -e
```
```
@reboot sh /home/pi/RaspberryPi-Projects/LCD-IP-Address/launcher.sh
```
7. Restart your pi, and the IP Address will display at start up!

## Video 
https://www.youtube.com/watch?v=MmSqdnEyP-g
