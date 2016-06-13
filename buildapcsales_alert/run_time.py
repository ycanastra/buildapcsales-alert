import time
import os
import json

def getLastRunTime():
	f = open('buildapcsales_alert/data.json', 'r')
	data = json.load(f)
	f.close()

	lastRunTime = data['last_run_time']

	return lastRunTime

def updateRunTime():
	with open('buildapcsales_alert/data.json', 'r') as f:
		data = json.load(f)

	data['last_run_time'] = time.time()

	with open('buildapcsales_alert/data.json', 'w') as f:
		json.dump(data, f)
