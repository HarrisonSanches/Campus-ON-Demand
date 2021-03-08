import openstack
from openstack.config import loader
import sys
from openstack import connection

openstack.enable_logging(True, stream=sys.stdout)
config = loader.OpenStackConfig()

def create_connection_openstack(auth_url, region, project_name, username, password,
                      user_domain, project_domain):
    return openstack.connect(
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password,
        region_name=region,
        user_domain_name=user_domain,
        project_domain_name=project_domain,
        app_name='examples',
        app_version='1.0',
    )

