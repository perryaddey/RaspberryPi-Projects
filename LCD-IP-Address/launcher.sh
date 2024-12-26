#! /bin/bash

cd /                                  #takes you to home directory 
cd /home/perry/RaspberryPi-Projects/LCD-IP-Address      #type pwd in the command line to find the path to where getipaddress.py is located
python3 getipaddress.py 
cd /                                  #takes you back to the home directory after the IP address is displayed
