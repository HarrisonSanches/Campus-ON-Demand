import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")

print("Allow pings:")
example_sec_group = conn.network.create_security_group(
    name='openstacksdk-example-security-group')

print(example_sec_group)

example_rule = conn.network.create_security_group_rule(
    security_group_id=example_sec_group.id,
    direction='ingress',
    remote_ip_prefix='0.0.0.0/0',
    protocol='icmp',
    port_range_max=None,
    port_range_min=None,
    ethertype='IPv4')

print(example_rule)