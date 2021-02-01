import openstack
from openstack .config import loader
import sys

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()
conn = openstack.connect(cloud="devstack-admin")


EXAMPLE_IMAGE_NAME = "example_image"
print("Import Image:")
# Url where glance can download the image
uri = 'https://download.cirros-cloud.net/0.4.0/cirros-0.4.0-x86_64-disk.img'
# Build the image attributes and import the image.
image_attrs = {
    'name': EXAMPLE_IMAGE_NAME,
    'disk_format': 'qcow2',
    'container_format': 'bare',
    'visibility': 'public',
    }

image = conn.image.create_image(**image_attrs)
conn.image.import_image(image, method="web-download", uri=uri)