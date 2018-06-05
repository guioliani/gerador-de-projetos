import sys
import os 

sys.path.append('models')
from gerador import gerador

def main():
	os.system("cls")
	gerador()

try:
	main()
except(KeyboardInterrupt):
	os.system("cls")
	print ("Voce pressionou Ctrl+C ou Delete para interromper este programa!")

