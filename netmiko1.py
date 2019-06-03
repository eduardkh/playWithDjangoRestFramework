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

output = net_connect.send_command('show ip arp')
print(output)
