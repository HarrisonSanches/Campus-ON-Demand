import requests

def list_projects():
    url = "https://192.168.0.125:9999/osm/admin/v1/projects"

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Authorization": 'Bearer AkfZELr3KSRqBotP08arfWlfe4pACV7a'
    }

    response = requests.request("GET", url, headers=headers, data = payload, verify=False)

    print(response.text.encode('utf8'))
    print(response.status_code)
    
def list_projects_id():
    pass

def del_project(obj):

    url = "https://fgcn-backflip3.cs.upb.de:9999/osm/admin/v1/projects/" + obj.id

    payload = {}
    headers = {
        'Content-Type': ' application/json',
        'Accept': ' application/json',
        "Authorization": 'Bearer AkfZELr3KSRqBotP08arfWlfe4pACV7a'

    }

    response = requests.request("DELETE", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
