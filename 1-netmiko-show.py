#!/usr/bin/env python
from netmiko import Netmiko

# SSH Connection Details
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.55',
    'username': 'cisco',
    'password': 'cisco',
}

# Establish SSH to device and run show command
net_connect = Netmiko(**ios1)
output = net_connect.send_command('show version')
net_connect.disconnect()
print (output)