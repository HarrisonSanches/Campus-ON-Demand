import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")

print("Delete Network:")
example_network = conn.network.find_network(
    'openstacksdk-example-project-network')

for example_subnet in example_network.subnet_ids:
    conn.network.delete_subnet(example_subnet, ignore_missing=False)

conn.network.delete_network(example_network, ignore_missing=False)