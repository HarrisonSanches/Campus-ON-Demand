import openstack
from openstack .config import loader
import sys

def create_user_in_openstack(username, password, conn):
    user = conn.create_user(name=username, password=password, domain_id='default')
    return user


# list user
def list_user(conn):
    user = conn.identity.users()
    return user