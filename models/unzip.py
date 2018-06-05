import zipfile
import os
import time

def unzip(fullName):
	with zipfile.ZipFile(fullName, "r") as zip_ref:
		zip_ref.extractall()
		print("\nextraindo os arquivos")
		time.sleep(20)
	
	zip_ref.close()
	os.remove(fullName)