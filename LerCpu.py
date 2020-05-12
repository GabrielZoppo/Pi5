import paho.mqtt.publish as publish

import time
from time import localtime, strftime

import psutil 
import subprocess 

SERVER = "mqtt.thingspeak.com"

CHANNEL_ID = "1056037"
WRITE_API_KEY = "HX28CZ5VZ46Z0PKU"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY
client = MQTTClient("umqtt_client", SERVER)
sleep = 59 # Intervalo em segundos de cada postagem

net_sts = 0 
old_value = 0

while True:
    # Leitura dos sensores
	cpu_percent = psutil.cpu_percent(interval=1)
	

	old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
	time.sleep(1)
	new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
	net_sts = new_value - old_value

	# Tratamento de valores
	

	gpu_percent = gpu_percent.decode("utf-8") 
	gpu_percent = gpu_percent.split("\n")
	gpu_percent = gpu_percent[0].split(",")
	gpu_percent = gpu_percent[0].split("=")

	try:
		# Printa os valores enviados, data e status da conexão
		print("CPU %:", cpu_percent)

		print(strftime("%a, %d %b %Y %H:%M:%S", localtime()))

		params = "field1="+str(gpu_percent[1])

		payload "field1="+str(temp)
        client.connect()
        client.publish(topic, payload)
        client.disconnect()

	except:
		print("connection failed") # Em caso de erro de conexão

	time.sleep(sleep)