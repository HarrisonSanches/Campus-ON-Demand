from requests.api import head
from database.models import Services
from database import connection_db
import openstack
import requests
from OSM.project import * 
from OSM.tokens import tokens
from flask import Flask, request, jsonify, json
from VIO.clouds.Openstack import connection
from VIO.clouds.Openstack.Apis import keystone
from database.models import *
from openstack import *
from VIO.clouds.Openstack.Apis.neutron.security_group import *
from VIO.clouds.Openstack.Apis.neutron.network import *
from VIO.clouds.Openstack.Apis.keystone.user import *
from VIO.clouds.Openstack.Apis.keystone.project import *
from VIO.clouds.Openstack.Apis.nova.flavor import *
from VIO.clouds.Openstack.Apis.nova.instance import *
from VIO.clouds.Openstack.Apis.nova.VM import *
import secrets
from OSM.project.project_OSM import *
from VIO.clouds.Openstack.connection.connection import *
from urls import *
from database  import *


app = Flask(__name__)

@app.route('/authentication/', methods=['POST','GET', 'DELETE', 'UPDATE'])
def authentication():
    
    info_service = request.get_json()
    name = info_service['name']
    
    if request.method == 'POST':
        token = str(secrets.token_hex(15))
        # adicionar método para capturar a data corretamente
        # captturar erro do banco futuramente
        Services.insert(name=name, token=token,creation_date='2021-04-03').execute()
        connection_openstack = create_connection_openstack("http://192.168.0.116/identity", 'RegionOne', 'admin', 'admin','stack','default','default')
        connection_openstack.create_group(name, "description", domain='default')
        connection_openstack.close()
        
        return str(token)
                 
    elif request.method == "UPDATE":
        new_name = info_service['new_name']
        return Services.update({Services.name: new_name}).where(Services.name == name).execute()
    
    elif request.method == 'GET':
        return Services.select(Services.name)
        

@app.route("/user/", methods=['POST','GET', 'DELETE'])
def users():
    info_user = request.get_json()
    # autentificar serviço depois
    # token = info_user['token']
    username = info_user['username']
    password = info_user['password']
    name = info_user['name']
    # buscar serviceço pelo token
    service = info_user['service']
    connection_openstack = create_connection_openstack("http://192.168.0.116/identity", 
                                                       'RegionOne', 'admin', 'admin','stack',
                                                       'default','default')
    
    if request.method == "POST":
        user = create_user_in_openstack(username,password,connection_openstack)
        id_user = user.id
        User.insert(iduser =id_user, name = name, username = username, password = password,
                    creation_date ='2021-01-01')
        
        # procurar serviço no banco posteriormente
        connection_openstack.add_user_to_group(username, service)          
        return user
    
      
@app.route('/projects/', methods=['POST','GET', 'DELETE'])
def projects():
    info_user = request.get_json()
    # verificar token do serviço e autenticar
    token = info_user['token']
    username = info_user['username']
    project_name = info_user['project_name']


    # o outro token é do admin do osm, são 2 tokens! 
    # verificar token osm no banco futuramente
    admin_name = 'admin'
    password_admin_osm=  'admin'
    project_id_admin= 'admin'
    token_osm = "fdfsss"
    admin = True

    connection_openstack = create_connection_openstack("http://192.168.0.116/identity", 
                                                       'RegionOne', 'admin', 'admin',
                                                       'stack','default','default')

    if request.method == 'GET':
        # GET TEM QUE SER N O USUARIO OPENSTACK, O OSM VAI MOSTRAR TODOS OS PROJETOS
        pass
    
    elif request.method == 'POST':     
        exist = False
        for projects in connection_openstack.list_projects():
            if projects == project_name:
                exist = True
        if exist:
            return ("já existe esse projeto para esse usuário")
        else:
            create_project(username,project_name,"kkkkkkkkkkkkkkkkkkkk", connection_openstack)
            connection_openstack.close()
            # USER ADMIN DO OSM PRA FAZER ESSA REQ -- USAR TOKEN DO OSM                          
            resp = create_project_OSM(project_name, admin_name, password_admin_osm, project_id_admin, token_osm, admin)
            
            # estou assumindo que ele vai conseguir criar o projesto
            admin_id = '0ca53357-a73e-4eda-b278-bef4bfd7b170'
            url_associate = 'https://192.168.0.115:9999/osm/admin/v1/users/admin'
            data = tokens.create_token('admin', 'admin', 'admin')
            token = data.split()[2].strip()
            
            
            payload = {
                    "add_project_role_mappings": [
                        {
                        "project": project_name,
                        "role": 'project_admin'
                    }]    
                }
        
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                "Authorization": 'Bearer ' + token
            }  
            
            
            # VERIFICAR AMANHA ISSO AQUI
            resp = requests.request('PATCH',url_associate, headers=headers, json=payload,verify=False)
            
            # preciso salvar no banco
            
            return resp.text

# @app.route('/VNF/', methods=['POST','GET', 'DELETE'])
# def VNF():
#     pass

@app.route('/vim/', methods=['POST','GET', 'DELETE'])
def vim():
    # info_user = request.get_json()
    # token = info_user['token']
    # username = info_user['username']
    # password = info_user['password']
    # project_id = info_user['project_id']
    # name = info_user['name']
    # admin = info_user['admin']
    # project_name = info_user['project_name']
    # service = info_user['service']
    if request.method == 'POST':
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        
        payload = json.dumps({
            "name": "teste",
            "description": "lllkkkkkk",
            "vim_type": "Openstack",
            "vim_url": "http://192.168.0.116/identity/v3/",
            "vim_tenant_name": "admin",
            "vim_user": "admin",
            "vim_password": "stack",
            "config": {
                "additionalProp1": {}
                }
            })
        
        response = requests.request(method="POST",url=url_vim, 
                                    headers=headers, data=payload)
        return(response.text)


@app.route("/security_group/", methods=['POST','GET', 'DELETE'])
def security_groups():
    info_user = request.get_json()
    username = info_user['username']
    password = info_user['password']
    project_name = info_user['project_name']
    security_group_name = info_user['security_group_name']
    # connection_openstack = create_connection_openstack("http://192.168.0.116/identity", 'RegionOne', project_name,
    #                                                    username,password,'default','default')  
    if request.method == 'POST':
        security_group = create_security_groups(security_group_name, connection_openstack)
        connection_openstack.close()

        return security_group
    
    elif request.method == 'GET':
        security_group = get_security_groups(security_group_name, connection_openstack)
        connection_openstack.close()
        
        return security_group
    
    elif request.method == 'DELETE':
        confirm = del_security_groups(security_group_name, connection_openstack)
        connection_openstack.close()

        return confirm
    
# @app.route("/rules/", methods=['POST','GET', 'DELETE'])
# def rules():
#     pass    

    

        