import requests
from OSM.tokens import tokens
url = "https://192.168.0.125:9999/osm/admin/v1/projects"

def list_projects(username, password, project_id, token):
        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "Authorization": 'Bearer ' + token
        }        
        response = requests.request("GET", url, headers=headers, data = payload, verify=False)

        if response.status_code == 401:            
            data = tokens.create_token(username, password, project_id)
            token = data.split()[2].strip()
        
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                "Authorization": 'Bearer ' + token
            }
            response = requests.request("GET", url, headers=headers, data = payload, verify=False)
       
            return '{}\n {}'.format(response.text, token)
        
        return response
    
def list_projects_id():
    pass

def del_project():

    url = "http://fgcn-backflip3.cs.upb.de:9999/osm/admin/v1/projects/" + obj.id

    payload = {}
    headers = {
        'Content-Type': ' application/json',
        'Accept': ' application/json',
        "Authorization": 'Bearer AkfZELr3KSRqBotP08arfWlfe4pACV7a'

    }

    response = requests.request("DELETE", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
