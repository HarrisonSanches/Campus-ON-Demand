import openstack
from openstack .config import loader
import sys

# openstack.enable_logging(True, stream=sys.stdout)
# config = loader.OpenStackConfig()
# conn = openstack.connect(cloud="devstack-admin")

# print("Create Network:")
# example_network = conn.network.create_network(
#     name='openstacksdk-example-project-network')

# print(example_network)
# example_subnet = conn.network.create_subnet(
#     name='openstacksdk-example-project-subnet',
#     network_id=example_network.id,
#     ip_version='4',
#     cidr='10.0.2.0/24',
#     gateway_ip='10.0.2.1')
# print(example_subnet)



# print("Delete Network:")
# example_network = conn.network.find_network(
#     'openstacksdk-example-project-network')

# for example_subnet in example_network.subnet_ids:
#     conn.network.delete_subnet(example_subnet, ignore_missing=False)

# conn.network.delete_network(example_network, ignore_missing=False)