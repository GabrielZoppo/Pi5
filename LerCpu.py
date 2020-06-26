import paho.mqtt.publish as publish
import time
from time import localtime, strftime
import serial
import psutil 
import subprocess 

SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "1056037"
WRITE_API_KEY = "HX28CZ5VZ46Z0PKU"
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
ser = serial.Serial('/dev/ttyUSB0', 9600)

sleep = 59 # Intervalo em segundos de cada postagem


while True:
    # Leitura dos sensores
	cpu_percent = psutil.cpu_percent(interval=1)
	if cpu_percent < 75:
		var = 1
		
		ser.write('1')
	else:
		 var = 0

	try:
		# Printa os valores enviados, data e status da conexão
		print("CPU %:", var)

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		params = "field2="+str(var)
		publish.single(topic,payload=params,hostname=SERVER)

	except:
		print("connection failed") # Em caso de erro de conexão

		time.sleep(sleep)
