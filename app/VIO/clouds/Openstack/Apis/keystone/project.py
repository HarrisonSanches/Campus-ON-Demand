import openstack
from openstack .config import loader
import sys

def create_project(username, project_name, description, conn):

    # CRIANDO O PROJETO
    conn.identity.create_project(name=project_name, description=description)
    role = 'member'
    role = conn.identity.find_role(role)  
    user = conn.identity.find_user(username)
    project = conn.identity.find_project(project_name)

    # ASSOCIANDO UM PROJETO A UM USUÁRIO E SUA DETERMINADA FUNÇÃO
    conn.identity.assign_project_role_to_user(project, user, role)
