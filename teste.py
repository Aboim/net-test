
import requests

timeout = 1

try:
    requests.head("http://www.google.com/", timeout=timeout)
    # Do something
    print('The internet connection is active')
except requests.ConnectionError:
    # Do something
    print("The internet connection is down")

# import module
import subprocess

# Traverse the ipconfig information
data = subprocess.check_output(['ipconfig', '/all']).decode('latin').split('\n')

# Arrange the bytes data
for item in data:
    print(item.split('\r')[:-1])
