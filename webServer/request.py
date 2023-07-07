import requests

url = 'http://10.30.60.15:3000/call-function'
data = {
    'functionName': "active",
}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.text
    print('Response:', result)
else:
    print('Error:', response.text)