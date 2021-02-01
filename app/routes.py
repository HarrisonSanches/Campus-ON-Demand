from requests.models import Response
import requests
from OSM.project import project
from OSM.tokens import tokens

from flask import Flask, request, jsonify, json
app = Flask(__name__)

url = "https://192.168.0.125:9999/osm/admin/v1/projects"

@app.route('/projects', methods=['POST','GET', 'DELETE'])
def projects():
    if request.method == 'GET':
        info_user = request.get_json()
        token = info_user['token']
        username = info_user['username']
        password = info_user['password']
        project_id = info_user['project_id']
        
        resp = project.list_projects(username,password, project_id, token)
        return resp
    elif request.method == 'POST':
        print("tem que fazer ainda")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Accept': 'application/json',
        #     "Authorization": 'Bearer ' + token
        # }
        
        # response = requests.request("GET", url, headers=headers, data = payload, verify=False)

        # if response.status_code == 401:
        #     username = info_user['username']
        #     password = info_user['password']
        #     project_id = info_user['project_id']
            
        #     data = tokens.create_token(username, password, project_id)
        #     token = data.split()[2].strip()
        #     print("TOKEN: ", token)
        
        #     payload = {}
        #     headers = {
        #         'Content-Type': 'application/json',
        #         'Accept': 'application/json',
        #         "Authorization": 'Bearer ' + token
        #     }
        #     response = requests.request("GET", url, headers=headers, data = payload, verify=False)
       
        #     return  response.text

        # # return  '{} {} {}'.format(response.text, response.status_code, token)
        # return response

        