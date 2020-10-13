import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")



EXAMPLE_IMAGE_NAME = "example_image"

print("List Images:")
for image in conn.image.images():
    print(image.name)

print("Delete Image:")
example_image = conn.image.find_image(EXAMPLE_IMAGE_NAME)
conn.image.delete_image(example_image, ignore_missing=False)