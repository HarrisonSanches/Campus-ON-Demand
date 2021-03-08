import openstack
from openstack .config import loader
import sys

def create_security_groups(security_group_name,conn):
    example_sec_group = conn.network.create_security_group(
        name=security_group_name)

    return example_sec_group

def get_security_groups(security_group_name, conn):
    security_group = conn.get_security_group(security_group_name)
    
    return security_group


def list_security_groups(conn):
    groups = conn.list_security_groups()
    return groups


def del_security_groups(security_group_name,conn):
    confirm = conn.delete_security_group(security_group_name)
    return confirm
