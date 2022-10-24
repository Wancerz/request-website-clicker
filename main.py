import requests
import time

while 1:

    time.sleep(2)
    response = requests.get('http://192.168.4.1/onD0')
    time.sleep(2)
    response = requests.get('http://192.168.4.1/offD0')

