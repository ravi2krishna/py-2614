# External Module Use Case 
# r = requests.get('https://www.python.org/') # NameError: name 'requests' is not defined
# print("HTTP Status Code: ",r.status_code)

import requests # ModuleNotFoundError: No module named 'requests'
r = requests.get('https://www.python.org/') 
print("HTTP Status Code: ",r.status_code)

# pip install requests 

import requests # ModuleNotFoundError: No module named 'requests'
r = requests.get('https://www.python.org/ravi') 
print("HTTP Status Code: ",r.status_code)

# if api is working do further processing
import requests 
r = requests.get('https://www.python.org/ravi') 
status_code = r.status_code
if status_code == 200:
    print("api is working doing further processing")
else:
    print("api is not working, stop further processing")