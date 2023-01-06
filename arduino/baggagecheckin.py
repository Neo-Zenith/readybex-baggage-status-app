import serial
import time
import requests
import ast

def formatData(data):
	data = "".join(data.split())
	data = data.lstrip('b')
	data = data.strip("'")
	data = data.rstrip("\\r\\n")
	return data

def readAndFormat(device):
	data=str(device.readline())
	formattedData = formatData(data)
	return formattedData

def checkInAPI(name, passportNo, bookingNo, status, airline, serialID):
	URL = "https://escendo.azurewebsites.net/api/v1/checkIn" # I AM NOT SURE IF THIS IS CORRECT
	headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"}

	data = {'name': name,
			'passportNo': passportNo,
			'bookingNo': bookingNo,
			'checkInExtended': {
				'airline': airline,
				'status': status,
				'serialID': serialID
				}
			}
  
	r = requests.post(url = URL, headers = headers, json = data)
	if r.status_code == 200:
		response = ast.literal_eval(r.text)
		if response["error"] ==  "error_OK":
			return True
		else:
			return False
	else:
		return False


def main(name, passportNo):
	connectionSuccess = 0
	port = 'COM7' #CHANGE THIS TO THE SERIAL PORT THAT THE ARDUINO IS CONNECTED TO
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
					bookingNo = readAndFormat(arduino)  #field1
					flightNo = readAndFormat(arduino) #field2
					status = "Checked In"
					print(bookingNo, flightNo, sID)
					if checkInAPI(name, passportNo, bookingNo, status, flightNo, sID):
						return True

			except Exception as e:
				print (e)
      
