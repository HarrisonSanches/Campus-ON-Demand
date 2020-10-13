import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")

print("----------Networks----------")
for network in conn.network.networks():
    print(network)

print("----------Subnets----------")
for subnet in conn.network.subnets():
    print(subnet)

print("----------Ports----------")
for port in conn.network.subnets():
    print(port)

print("----------Security Groups----------")
for group in conn.network.security_groups():
    print(group)

print("----------Routers----------")
for router in conn.network.routers():
    print(router)

print("----------Networks Agents----------")
for agent in conn.network.agents():
    print(agent)

