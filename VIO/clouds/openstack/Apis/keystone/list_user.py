import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
confgid = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")


for user in conn.identity.users():
    print(user.name)