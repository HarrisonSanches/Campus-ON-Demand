from openstack import identity
from openstack.exceptions import OpenStackCloudException
from peewee import DateField, Model
import requests
import openstack
from openstack.config import loader
import sys
from openstack import connection
import mysql.connector
from database.connection_db import create_connection_db
from database.models import *
from VIO.clouds.Openstack.connection.connection import create_connection_openstack
import secrets
from openstack import exceptions 
# cnx = create_connection_db('orchestrator_database', 'root', 'root', '127.0.0.1', 3306)


token = secrets.token_hex(15)
print(str(token))

connection_openstack = create_connection_openstack("http://192.168.1.108/identity", 'RegionOne', 'test',
                                                'test','test123','default','default')

# a = connection_openstack.delete_security_group('test4')

# try:
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
