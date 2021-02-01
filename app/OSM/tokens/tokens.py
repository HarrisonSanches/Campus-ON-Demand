import requests
url = "https://192.168.0.125:9999/osm/admin/v1/tokens"

def create_token(username, password, project_id):
    headers = {
    'Content-Type': 'application/json'
    }
    payload = {
        "username": username,
	    "password": password,
	    "project_id": project_id
    }

    response = requests.request("POST", url, headers=headers, json = payload, verify=False)
    print("RESPOSTA DO TOKEN: ", response.text)
    
    return response.text
    
    
    
        # verificar se o token é valido (função) 
    



