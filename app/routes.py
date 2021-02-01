from requests.models import Response
import requests
from OSM.project import project
from OSM.tokens import tokens
from flask import Flask, request, jsonify, json

app = Flask(__name__)
url = "https://192.168.0.125:9999/osm/admin/v1/projects"

@app.route('/projects', methods=['POST','GET', 'DELETE'])
def projects():
    info_user = request.get_json()
    token = info_user['token']
    username = info_user['username']
    password = info_user['password']
    project_id = info_user['project_id']
    name = info_user['name']
    admin = info_user['admin']
    
    if request.method == 'GET':
        resp = project.list_projects(username,password, project_id, token)
        return resp
    elif request.method == 'POST':
        print("PROJECT NAME---------->>>>", name)

        resp = project.create_project(username, password, project_id, token, name, admin)
        return resp


    


        