#!/usr/bin/env python
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(
    config_file="config.yml", dry_run=True
)

result = nr.run(netmiko_send_command, command_string="show ip int brief")

print_result(result)