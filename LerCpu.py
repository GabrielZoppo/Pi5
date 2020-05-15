import paho.mqtt.publish as publish

import time
from time import localtime, strftime

import psutil 
import subprocess 

SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "1056037"
WRITE_API_KEY = "HX28CZ5VZ46Z0PKU"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
sleep = 59 # Intervalo em segundos de cada postagem


while True:
    # Leitura dos sensores
	cpu_percent = psutil.cpu_percent(interval=1)
	

	try:
		# Printa os valores enviados, data e status da conexão
		print("CPU %:", cpu_percent)

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		params = "field1="+str(cpu_percent)
		
        

	except:
		print("connection failed") # Em caso de erro de conexão

	time.sleep(sleep)
