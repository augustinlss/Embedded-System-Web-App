import requests
import serial

arduinoData = serial.Serial('/dev/tty.usbmodem142201', 115200)
currentCmd = ""

while True:
    dataPacket = arduinoData.readline().decode('utf-8').rstrip()
    if dataPacket == 'active':
        data = {
            'functionName': dataPacket,
        }
        #10.30.60.15 for guest
        #131.155.122.29 for wpa2
        response = requests.post('http://10.30.60.15:3000/call-function', json=data)
        print(response.text)
        dataPacket = response.text
        arduinoData.write(dataPacket.encode())
    if (dataPacket == "0 " or dataPacket == "1" or dataPacket == "-1" or dataPacket == 'white init' or dataPacket == 'black init') and currentCmd != dataPacket:
        currentCmd = dataPacket
        data = {
            'functionName': dataPacket,
        }
        #10.30.60.15 for guest
        #131.155.122.29 for wpa2
        response = requests.post('http://10.30.60.15:3000/call-function', json=data)
        print(response.text)
        dataPacket = response.text
    