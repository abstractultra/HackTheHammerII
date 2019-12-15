import requests
from time import sleep

while True:
    try:
        requests.get("http://localhost:8000/update", timeout=0.1)
    except requests.exceptions.ReadTimeout:
        print ("ok")
        sleep (5)