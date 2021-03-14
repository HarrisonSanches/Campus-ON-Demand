# import openstack
# from openstack .config import loader
# import sys

# openstack.enable_logging(True, stream=sys.stdout)
# config = loader.OpenStackConfig()
# conn = openstack.connect(cloud="devstack-admin")

# flavor_teste = conn.compute.create_flavor(
#     name = 'flavor_teste',
#     vcpus = 2,
#     disk = 40,
#     ram = 1024,
#     ephemeral = 0,
#     is_public = True)