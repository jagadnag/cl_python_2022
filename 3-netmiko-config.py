#!/usr/bin/env python
from netmiko import Netmiko

# SSH Connection Details
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.55',
    'username': 'cisco',
    'password': 'cisco',
}

ios2 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.56',
    'username': 'cisco',
    'password': 'cisco',
}

devices = [ios1, ios2]

for device in devices: 
    # Establish SSH to device and run config command
    print ('Connecting to device ' + device['ip'])
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set('logging host 10.1.1.2')
    net_connect.disconnect()
    print (output)
