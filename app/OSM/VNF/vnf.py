import requests

def create_vnf(obj):
    url = "https://192.168.0.125:9999/osm/admin/v1/vnf_packages"

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Authorization": 'Bearer AkfZELr3KSRqBotP08arfWlfe4pACV7a'
    }

    response = requests.request("POST", url, headers=headers, data = payload, verify=False)

    print(response.text.encode('utf8'))
    print(response.status_code)




# Verificar possibilidade de usuarios com uma unica vim
#usar django (experimentar) 


# -----------------------EXEMLO DE VFN-----------------------------#
    vnf = {
    "vnfd": {
        "description": "Simple VNF example with a cirros and a VNF alarm",
        "df": [
        {
            "id": "default-df",
            "instantiation-level": [
            {
                "id": "default-instantiation-level",
                "vdu-level": [
                {
                    "number-of-instances": 1,
                    "vdu-id": "cirros_vnfd-VM"
                }
                ]
            }
            ],
            "vdu-profile": [
            {
                "id": "cirros_vnfd-VM",
                "min-number-of-instances": 1
            }
            ]
        }
        ],
        "ext-cpd": [
        {
            "id": "eth0-ext",
            "int-cpd": {
            "cpd": "eth0-int",
            "vdu-id": "cirros_vnfd-VM"
            }
        }
        ],
        "id": "cirros_alarm-vnf",
        "mgmt-cp": "eth0-ext",
        "product-name": "cirros_alarm-vnf",
        "provider": "OSM",
        "sw-image-desc": [
        {
            "id": "cirros-0.3.5-x86_64-disk.img",
            "image": "cirros-0.3.5-x86_64-disk.img",
            "name": "cirros-0.3.5-x86_64-disk.img"
        }
        ],
        "vdu": [
        {
            "alarm": [
            {
                "actions": {
                "alarm": [
                    {
                    "url": "${WEBHOOK_URL}"
                    }
                ],
                "insufficient-data": [
                    {
                    "url": "${WEBHOOK_URL}"
                    }
                ],
                "ok": [
                    {
                    "url": "${WEBHOOK_URL}"
                    }
                ]
                },
                "alarm-id": "alarm-1",
                "operation": "LT",
                "value": 20,
                "vnf-monitoring-param-ref": "cirros_vnf_cpu_util"
            }
            ],
            "description": "cirros_vnfd-VM",
            "id": "cirros_vnfd-VM",
            "int-cpd": [
            {
                "id": "eth0-int",
                "virtual-network-interface-requirement": [
                {
                    "name": "eth0",
                    "virtual-interface": {
                    "bandwidth": 0,
                    "type": "VIRTIO",
                    "vpci": "0000:00:0a.0"
                    }
                }
                ]
            }
            ],
            "monitoring-parameter": [
            {
                "id": "cirros_vnf_cpu_util",
                "name": "cirros_vnf_cpu_util",
                "performance-metric": "cpu_utilization"
            },
            {
                "id": "cirros_vnf_average_memory_utilization",
                "name": "cirros_vnf_average_memory_utilization",
                "performance-metric": "average_memory_utilization"
            }
            ],
            "name": "cirros_vnfd-VM",
            "sw-image-desc": "cirros-0.3.5-x86_64-disk.img",
            "virtual-compute-desc": "cirros_vnfd-VM-compute",
            "virtual-storage-desc": [
            "cirros_vnfd-VM-storage"
            ]
        }
        ],
        "version": "1.0",
        "virtual-compute-desc": [
        {
            "id": "cirros_vnfd-VM-compute",
            "virtual-cpu": {
            "num-virtual-cpu": 1
            },
            "virtual-memory": {
            "size": 0.25
            }
        }
        ],
        "virtual-storage-desc": [
        {
            "id": "cirros_vnfd-VM-storage",
            "size-of-storage": 2
        }
        ]
    }
    }