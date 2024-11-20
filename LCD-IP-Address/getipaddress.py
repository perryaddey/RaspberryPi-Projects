
import subprocess
import LCD1602
from time import sleep

sleep(20)
LCD1602.init(0x27, 1)
LCD1602.clear()

def getip():
	command = "hostname -I"
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	output = proc.stdout.read()
	output = output.split()
	output = str(output[0])
	output = output.split("'")
	return output[1]

ipaddress = getip()
LCD1602.write(0,0, 'IP Address')
LCD1602.write(0,1, ipaddress)
