#! Python3

from urllib import request
import requests
from getpass import getpass 

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
requests.get('https://api.github.com/user', auth=('AaronHaws', getpass()))
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
requests.post('https://api.github.com')
# this is a test
requests.put('https://api.github.com')

requests.delete('https://api.github.com')

requests.head('https://api.github.com')




