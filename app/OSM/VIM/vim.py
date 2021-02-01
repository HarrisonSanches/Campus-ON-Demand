import requests


def get_vim_accounts(obj):
    
    url = "https://fgcn-backflip3.cs.upb.de:9999/osm/admin/v1/wim_accounts"

    payload = {}
    headers = {
        'Content-Type': ' application/json',
        'Accept': ' application/json',
        "Authorization": obj.token
    }

    response = requests.request("GET", url, headers=headers, data = payload,verify=False)

    print(response.text.encode('utf8'))
    
def create_vim(obj):
    url = "https://fgcn-backflip3.cs.upb.de:9999/osm/admin/v1/wim_accounts"
    vim = {
        "schema_version": "1.11",
        "name": "openstack-site",
        "description": "nuvem openstack",
        "vim_type": "openvim",
        "vim_url": "http://192.168.0.126/identity/v3",
        "vim_tenant_name": "admin",
        "vim_user": "admin",
        "vim_password": "stack",
        "config": {
            "additionalProp1": {"Security Groups": "default"}
        }
    }
    
    headers = {
        'Content-Type': ' application/json',
        'Accept': ' application/json',
        "Authorization": 'Bearer AkfZELr3KSRqBotP08arfWlfe4pACV7a'

    }
    
    response = requests.request("POST", url, headers=headers, json = vim, verify=False)

    print(response.text.encode('utf8'))
