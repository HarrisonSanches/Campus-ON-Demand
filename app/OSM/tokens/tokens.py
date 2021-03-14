import requests
url = "https://192.168.0.115:9999/osm/admin/v1/tokens"

def create_token(admin_name, password_admin, project_id_admin):
    headers = {
    'Content-Type': 'application/json'
    }
    payload = {
        "username": admin_name,
	    "password": password_admin,
	    "project_id": project_id_admin
    }

    response = requests.request(method="POST", url=url, headers=headers, json = payload, verify=False)
    print("RESPOSTA DO TOKEN: ", response.text)
    
    return response.text
    
    
    
        # verificar se o token é valido (função) 
    



