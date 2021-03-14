from openstack import identity
from openstack.exceptions import OpenStackCloudException
from peewee import DateField, Model
import requests
import openstack
from openstack.config import loader
import sys
from openstack import connection
import mysql.connector
# from database.connection_db import create_connection_db
# from database.models import *
# from VIO.clouds.Openstack.connection.connection import create_connection_openstack
import secrets
from openstack import exceptions 
# cnx = create_connection_db('orchestrator_database', 'root', 'root', '127.0.0.1', 3306)

from openstack.identity.v3._proxy import *
import yaml
import json
from app.VIO.clouds.Openstack.connection.connection import * 

# headers = {
#         'Accept':'application/json',
#         'Content-Type':'application/json'
#         }

# json pra criar usuario
# payload={'username': 'test1',
#          'password': 'test123',
#          'name': 'fulano',
#          'service': 'Campus-On-Demand'
#          }
# 

# json para criar projeto
payload={'username': 'test1',
        'project_name': 'projeto_test',
        #daqui pra baixo eu que tenho essas informações, nao precisa mandar
        'token': "kkkkkk"
        #  token pro admin do osm
        }


a = requests.request(method="POST", url='http://127.0.0.1:8000/projects/', json=payload)
print(a.text)
# url = 'https://192.168.0.115:9999/osm/admin/v1/projects'
# token_osm = 'SxAZEuYlSkGoAIVJpljr7lRUuhodoDRx'



# payload={}
# headers = {
#     'Content-Type': ' application/json',
#     'Accept': ' application/json',
#     "Authorization": 'Bearer ' + token_osm
# }

# response = requests.request("GET", url, headers=headers, json=payload)

# print(response.json())

# payload={
#     "username": "admin",
#     "password": "admin",
#     "project_id": "admin"
#         #  token pro admin do osm
#     }

# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, json=payload, verify=False)
# print(response.text)
# token = secrets.token_hex(15)
# # print(str(token))

# connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 'RegionOne', 'test',
#                                                 'test','test123','default','default')

# connection_openstack.list_projects()

# a = connection_openstack.get_project("test")
# print(a.name)

# with open("/home/sanches/Downloads/yaml-validator.yaml", 'r') as yaml_in, open("example.json", "w") as json_out:
#     yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
#     json.dump(yaml_object, json_out)

# b = open('/home/sanches/projects/Campus-ON-Demand/example.json',)
# c = json.load(b)

# for item in c:
#     item['prices'][0]['price'] = 200
    
# print(c)


# sys.stdout.write(yaml.dump(json.load(b)))
# print(b)
# print('saída')
# print()

# a = open("/home/sanches/Downloads/yaml-validator.yaml",)

# b = yaml.full_load(a)

# b[0]['prices'][0]['price'] = 200
# b[1]['prices'][0]['price'] = 550

# sys.stdout.write(yaml.dump(b))
       
            # try:s
# a = connection_openstack.create_user(name="username", password="password", domain_id='default')
# except identity. as e:
#     print("HUIASHSASAHDSA")
#     print(e)
# print(a)

# print("AAAA")
# print(a)
# print()
# print("sadASADSADSA")
# for item in connection_openstack.list_security_groups():
#     print(item.name)

# security_group = connection_openstack.network.create_security_group(
#         name='test4')
# print()
# print("AAASDAAS")
# print(security_group.name)

# print()
# print("result")
# print(security_group)
# test = connection_openstack.get_security_group('default')

# print()
# print("results")
# print(test.name, test.id)

# test = Services.select(Services.name)
# for item in test:
#     name = item.name
# # print(name)
# connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 'RegionOne', 'admin', 'admin','stack','default','default')
# connection_openstack.create_group(name, "description", domain='default')



# cnx = create_connection_db('127.0.0.1', 3306, 'root','root','orchestrator_database')
# cnx = create_connection_db('orchestrator_database', 'root', 'root', '127.0.0.1', 3306)

# q = ((Services.insert(name="Campus ON Demand", token='abc123',creation_date='2021-04-03')).execute())

# test = Services.select(Services.name)

# for service in test:
#     print(service.name)

# url = "https://192.168.0.125:9999/osm/admin/v1/users"
# token = 'zKTzCn5a3cajfeI2psKjKF4tao2KpgNF'
# headers = {
# "Authorization": 'Bearer zKTzCn5a3cajfeI2psKjKF4tao2KpgNF'
# }

# user = {
#     "username": "teste",
#     "password": "123456",
# }

# response = requests.request("POST", url, headers=headers, json = user)
# print(response.status_code)
    


# openstack.enable_logging(True, stream=sys.stdout)
# config = loader.OpenStackConfig()



# def create_connection(auth_url, region, project_name, username, password,
#                       user_domain, project_domain):
#     return openstack.connect(
#         auth_url=auth_url,
#         project_name=project_name,
#         username=username,
#         password=password,
#         region_name=region,
#         user_domain_name=user_domain,
#         project_domain_name=project_domain,
#         app_name='examples',
#         app_version='1.0',
#     )

# connection = connection.Connection(auth_url = "http://192.168.1.108/identity", project_name= 'admin', username= 'admin', password='stack', user_domain_id='default', project_domain_id='default')


# projeto_teste = connection.identity.create_project(name="projeto_teste2",
#     description='projeto de teste')

# role = connection.identity.find_role("member")  
# user = connection.identity.find_user("admin")
# project = connection.identity.find_project("projeto_teste2")

# connection.identity.assign_project_role_to_user(project, user, role)

# for projects in connection.identity.projects():
    # print(projects.name)
# teste = connection.compute.





# ASSOCIANDO UM PROJETO A UM USUÁRIO E SUA DETERMINADA FUNÇÃO
# connection.identity.a('projeto_teste', 'admin', 'member')

    #   auth_url: http://192.168.1.108/identity
    #   password: stack
    #   project_domain_id: default
    #   project_name: alt_demo
    #   user_domain_id: default
    #   username: alt_demo
    # identity_api_version: '3'
    # region_name: RegionOne
    # volume_api_version: '3'

# url = "http://127.0.0.1:5000/projects"
# headers = {
#     'Content-Type': 'application/json'
# }
# payload = {
#     "username": "admin",
#     "password": "admin",
#     "project_id": "admin", 
#     "token": 'kkkkkkkkkkkkkkkkkkkkkk',
#     "name": "projeto teste",
#     "admin": False
# }

# response = requests.request('GET', url, headers=headers, json=payload, verify=False)
