import json
import requests
import sys
import os 
import time
import urllib.request
from unzip import unzip

def gerador():
	argumentos = sys.argv
	contem = False

	with urllib.request.urlopen('http://mmhand.esy.es/deped/states.json') as f:
		data = json.loads(f.read().decode())

	for state in data[argumentos[1]]:
		if(argumentos[2] in state['version']):
			contem = True
			dados = state['name'] + "-" + state['version'] + " " + state['link']
			fullName = state['name'] + "-" + state['version'] + "." + state['extension']
			link = state['link']
			extension = state['extension']

	if (contem):
		#print(state['name'], state['version'], state['link'])
		print("Gerando " + fullName)
		url = link
		r = requests.get(url, allow_redirects=True)
		
		total = len(r.content)
		dl = 0
		start = time.clock()

		for chunk in r.iter_content(1024):
			dl += len(chunk)
			open(fullName, 'wb').write(r.content)
			done = int(50 * dl / total)
			sys.stdout.write("\r[%s%s] %s bps" % ('▀' * done, ' ' * (50-done), dl//(time.clock() - start)))

		if(extension == 'zip'):
			unzip(fullName)
		else:
			print("\nDownload feito com sucesso")
	else:
		print("nao tem")