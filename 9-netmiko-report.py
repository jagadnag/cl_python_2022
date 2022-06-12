#!/usr/bin/env python
from netmiko import Netmiko
from pprint import pprint

# SSH Connection Details
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.1.55',
    'username': 'cisco',
    'password': 'cisco',
}

# Establish SSH to device and run show command
net_connect = Netmiko(**ios1)
output = net_connect.send_command('show version', use_genie=True)
net_connect.disconnect()
print(output)

print()
pprint(output)
print()