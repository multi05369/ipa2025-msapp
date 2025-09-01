import os
import netmiko
import ntc_templates
from dotenv import load_dotenv
load_dotenv()

def connection(ip : str, username : str, password : str):
    '''Connect to Cisco router via Netmiko'''
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': username,
        'password': password,
        "use_keys": False,
        "allow_agent": False,
    }
    return netmiko.ConnectHandler(**device)
