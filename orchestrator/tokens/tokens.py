import requests

url = "https://131.234.29.187:9999/osm/admin/v1/tokens"


def create_token(url):
    

    payload = "{\n\t\"username\": \"admin\",\n\t\"password\": \"admin\",\n\t\"project_id\" : \"{{project_id}}\"\n}"
    headers = {
    'Content-Type': 'application/json'
    }
    payload = {
        "username": "admin",
	    "password": "admin",
	    "project_id" : "admin"   
    }

    response = requests.request("POST", url, headers=headers, json = payload)

    print(response.text.encode('utf8'))
    print(response.status_code)
    
    



