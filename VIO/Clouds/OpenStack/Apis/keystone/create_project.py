import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")


role = conn.identity.find_role("member")  
user = conn.identity.find_user("user_teste")
project = conn.identity.find_project("projeto_teste")

# CRIANDO O PROJETO
projeto_teste = conn.identity.create_project(name="projeto_teste",
    description='projeto de teste')


# ASSOCIANDO UM PROJETO A UM USUÁRIO E SUA DETERMINADA FUNÇÃO
conn.identity.assig_project_role_to_user(project, user, role)
