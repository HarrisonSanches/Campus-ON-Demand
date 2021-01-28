import requests

# url = "https://192.168.0.125:9999/osm/admin/v1/users"

def list_user_OSM(url, json):

    payload = {}
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Authorization": 'Bearer AkfZELr3KSRqBotP08arfWlfe4pACV7a'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    print(response.status_code)

def create_user_OSM(url, obj):
   
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Authorization": 'Bearer 4b1pUs1QH0kzEwpXD76xWjbomd3uSuRr'
    }

    user = {
        "username": obj.username,
        "password": obj.password,
        "projects": obj.projects,
        "project_role_mappings": obj.project_role_mappings
    }


    response = requests.request("POST", url, headers=headers, json = user, verify =False)

    print(response.text.encode('utf8'))
    print(response.status_code)

def del_user(obj):
    url = "https://192.168.0.125:9999/osm/admin/v1/users/" + obj.id 
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    "Authorization": 'Bearer 4b1pUs1QH0kzEwpXD76xWjbomd3uSuRr'
    }
    response = requests.request("DELETE", url, headers=headers, data = payload, verify =False)
    

#     "username": "sanches",
#     "password": "123456",
#     "projects": [ 
#         "test"
#     ],
#     "project_role_mappings": [
#     {
#         "project": "test",
#         "role": "project_user"
#     }
#     ]
# }