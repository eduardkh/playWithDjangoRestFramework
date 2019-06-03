from netmiko import ConnectHandler


cisco_881 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.253',
    'username': 'cisco',
    'password': 'cisco',
    # 'port' : 8022,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
    'verbose': False,       # optional, defaults to False
}

net_connect = ConnectHandler(**cisco_881)

config_commands = ['interface l0',
                   'ip address 1.1.1.1 255.255.255.0',
                   'do show ip interface br | i 1.1.1.1']

output = net_connect.send_config_set(config_commands)
print(output)
