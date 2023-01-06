import requests
import serial
import time
from baggagecheckin import *

def statusUpdateAPI(serialID, status):
    URL = "https://escendo.azurewebsites.net/api/v1/statusUpdate" # I AM NOT SURE IF THIS IS CORRECT
    headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"}

    data = {'serialID': serialID,
            'status': status}
    
    r = requests.post(url = URL, headers = headers, json = data)
    if r.status_code == 200:
        return True
    else:
        return False


def main(status):
	connectionSuccess = 0
	port = 'COM6' #CHANGE THIS TO THE SERIAL PORT THAT THE ARDUINO IS CONNECTED TO
	try:
		print ("Trying to connect to", port+"...") 
		arduino = serial.Serial(port, 9600, timeout = 10) 
		connectionSuccess = 1
		print("Success!")
	except Exception as e:
		print(e) 
		print ("Failed to connect on", port)


	#main loop: use kill terminal to break out
	if(connectionSuccess == 1):
		while True:
			time.sleep(1)
			try:
				formattedData = readAndFormat(arduino)
				if (formattedData == "*"):
					sID = readAndFormat(arduino)
					print(sID, status)
					if statusUpdateAPI(sID, status):
						return True

			except Exception as e:
				print (e)


main("Checked in")
##main("Departed")
##main("Landed")
##main("Arrived")