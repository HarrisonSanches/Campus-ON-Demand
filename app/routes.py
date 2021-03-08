from logging import info
import openstack
from typing import MappingView
from VIO.clouds.Openstack.connection.connection import create_connection_openstack
import requests
from OSM.project import project
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

app = Flask(__name__)

@app.route('/authentication/', methods=['POST','GET', 'DELETE', 'UPDATE'])
def authentication():
    info_service = request.get_json()
    name = info_service['name']
    
    if request.method == 'POST':
        token = str(secrets.token_hex(15))
        # adicionar método para capturar a data corretamente
        Services.insert(name=name, token=token,creation_date='2021-04-03').execute()
        connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 'RegionOne', 'admin', 'admin','stack','default','default')
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
    token = info_user['token']
    username = info_user['username']
    password = info_user['password']
    name = info_user['name']
    connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 
                                                       'RegionOne', 'admin', 'admin','stack',
                                                       'default','default')
    
    if request.method == "POST":
        connection_openstack.identity.create_user()

        


      
@app.route('/projects/', methods=['POST','GET', 'DELETE'])
def projects():
    info_user = request.get_json()
    token = info_user['token']
    username = info_user['username']
    password = info_user['password']
    project_id = info_user['project_id']
    name = info_user['name']
    admin = info_user['admin']
    project_name = info_user['project_name']
    service = info_user['service']
    
    if request.method == 'GET':
        resp = project.list_projects(username,password, project_id, token)
        return resp
    elif request.method == 'POST':
        connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 'RegionOne', 'admin', 'admin','stack','default','default')
        
        for user in connection_openstack.user():
            # verificar se é username ou username
            # Verificando se o usuário já existe no Openstack
            if user.name == username:
                exist = False
                for projects in connection_openstack.projects():
                    if projects == project_name:
                        exist == True
                if exist:
                    return ("já existe esse projeto para esse usuário")
                else:
                    create_project(username,project_name,"SHJNISOJDIOPASJDIOAS", connection_openstack)                              
                    resp = project.create_project(username, password, project_id, token, name, admin)
                    return resp
        # Caso não exista, eu crio o usuário no openstack e em seguida crio projeto no OSM
        
        # MUDAR O ARQUIVO CREATE USER NO VIO URGENTE
        # MUDAR PARA PROCURAR O SERVICEO NO BANCO, SEM QUE SEJA NECESSÁRIO ENVIAR UMA REQUISIÇÃO PRA ISSO
        # UTILIZAR O TOKEN PARA ESSA CONSULTA
        connection_openstack.identity.create_user(name=name, password=password)
        create_project(username,project_name,"SHJNISOJDIOPASJDIOAS", connection_openstack)                              
        connection_openstack.add_user_to_group(username, service)

        resp = project.create_project(username, password, project_id, token, name, admin)
        connection_openstack.close()
        return resp

@app.route('/VNF/', methods=['POST','GET', 'DELETE'])
def VNF():
    pass

@app.route('/vim/', methods=['POST','GET', 'DELETE'])
def vim():
    info_user = request.get_json()
    token = info_user['token']
    username = info_user['username']
    password = info_user['password']
    project_id = info_user['project_id']
    name = info_user['name']
    admin = info_user['admin']
    project_name = info_user['project_name']
    service = info_user['service']

    pass

@app.route("/security_group/", methods=['POST','GET', 'DELETE'])
def security_groups():
    info_user = request.get_json()
    username = info_user['username']
    password = info_user['password']
    project_name = info_user['project_name']
    security_group_name = info_user['security_group_name']
    connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 'RegionOne', project_name,
                                                       username,password,'default','default')  
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
    
@app.route("/rules/", methods=['POST','GET', 'DELETE'])
def rules():
    pass    

    

        