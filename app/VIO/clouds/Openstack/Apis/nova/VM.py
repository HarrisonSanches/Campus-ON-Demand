# import openstack
# from openstack .config import loader
# import sys

# openstack.enable_logging(True, stream=sys.stdout)
# config = loader.OpenStackConfig()
# conn = openstack.connect(cloud="devstack-admin")


# # IMAGE NAME, FLAVOR_NAME e NETWORK_NAME DEVEM SER PASSADOS
# print("Create Server:")
# image = conn.compute.find_image()
# flavor = conn.compute.find_flavor()
# network = conn.network.find_network()
# keypair = create_keypair(conn)

# server = conn.compute.create_server(
#     name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
#     networks=[{"uuid": network.id}], key_name=keypair.name)
# server = conn.compute.wait_for_server(server)

# print("ssh -i {key} root@{ip}".format(
#     key=PRIVATE_KEYPAIR_FILE,
#     ip=server.access_ipv4))