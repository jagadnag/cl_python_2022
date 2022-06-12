#!/usr/bin/env python
import os
from netmiko import Netmiko


# Sending device ip's stored in a file 
with open('device_list') as f:
    device_list = f.read().splitlines()

# Iterate through device list and configure the devices 
for device in device_list:
    print ('Connecting to device ' + device)
    ip_address_of_device = device
    
    # SSH Connection details 
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': 'cisco',
        'password': 'cisco'
    }
 
    net_connect = Netmiko(**ios_device)
    output = net_connect.send_config_from_file('reset_config')
    print (output)

if os.path.exists("backup/iosv-1.cfg"):
  os.remove("backup/iosv-1.cfg")

if os.path.exists("backup/iosv-2.cfg"):
  os.remove("backup/iosv-2.cfg")  

if os.path.exists("backup/iosv-1.txt"):
  os.remove("backup/iosv-1.txt")

if os.path.exists("backup/iosv-2.txt"):
  os.remove("backup/iosv-2.txt")  

if os.path.exists("inventory.csv"):
  os.remove("inventory.csv")

print()
print("*" * 80)
print ("Lab reset to default config..")
print("*" * 80)
print()