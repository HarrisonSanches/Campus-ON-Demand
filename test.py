# import requests


# url = "https://192.168.0.125:9999/osm/admin/v1/users"
# token = 'zKTzCn5a3cajfeI2psKjKF4tao2KpgNF'
# headers = {
# "Authorization": 'Bearer zKTzCn5a3cajfeI2psKjKF4tao2KpgNF'
# }

# user = {
#     "username": "teste",
#     "password": "123456",
# }

# response = requests.request("POST", url, headers=headers, json = user)
# print(response.status_code)
    

import requests

url = "http://127.0.0.1:5000/projects"
headers = {
    'Content-Type': 'application/json'
}
payload = {
    "username": "admin",
    "password": "admin",
    "project_id": "admin", 
    "token": 'kkkkkkkkkkkkkkkkkkkkkk',
    "name": "Teste 2",
    "admin": False
}

response = requests.request('POST', url, headers=headers, json=payload, verify=False)

print(response.text)