import openstack
from openstack .config import loader
import sys

def create_user_in_openstack(username, password, conn):
    user = conn.create_user(name=username, password=password, domain_id='default')
    return user


# get user
def get_user(username, conn):
    user = conn.get_user(username)
    return user