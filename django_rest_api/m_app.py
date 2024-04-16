import json
from types import SimpleNamespace

import requests

m_url= 'http://127.0.0.1:8000/api/animalapi/'
#
# r = requests.get(url= m_url)
# data = r.json()
# print(data)
#
#####POST METHOD
data= {'mid': 5, 'name': 'mungi', 'type': 'small', 'location': 'warool'}
json_data = json.dumps(data) #converting dict data to json
r = requests.post(url=m_url,data=data )
data =r.json()
print(data)
# def delete_data():
#     m_url = 'http://127.0.0.1:8000/api/animalapi/'
#
#     data = {
#         'mid':2,
#
#     }
#
#     json_data = json.dumps(data)
#     r = requests.delete(url=m_url, data=json_data)
#     data = r.json()
#     print(data)
# delete_data()