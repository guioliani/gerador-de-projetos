import json
import requests
import sys
import zipfile
import os 
import time
import urllib.request

argumentos = sys.argv
contem = False

def unzip():
	with zipfile.ZipFile(fullName, "r") as zip_ref:
		zip_ref.extractall()
		print("extraindo os arquivos")
		time.sleep(20)
	
	zip_ref.close()
	os.remove(fullName)

def deleta():
	os.remove(fullName)


with urllib.request.urlopen('http://mmhand.esy.es/deped/states.json') as f:
	data = json.loads(f.read().decode())

for state in data[argumentos[1]]:
	if(argumentos[2] in state['version']):
		contem = True
		dados = state['name'] + "-" + state['version'] + " " + state['link']
		fullName = state['name'] + "-" + state['version'] + "." + state['extension']
		link = state['link']

if (contem):
	#print(state['name'], state['version'], state['link'])
	print("Gerando " + dados)
	url = link
	r = requests.get(url, allow_redirects=True) 
	open(fullName, 'wb').write(r.content)
	print(len(r.content))
	unzip()
else:
	print("nao tem")

