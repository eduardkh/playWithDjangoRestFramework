from netmiko import ConnectHandler

HOSTS = [
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.253',
        'username': 'cisco',
        'password': 'cisco'
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.160',
        'username': 'cisco',
        'password': 'cisco'
    },
    {
        'device_type': 'cisco_ios',
        'ip': '192.168.122.101',
        'username': 'cisco',
        'password': 'cisco'
    }
]

for HOST in HOSTS:
    print('Accessing', HOST['ip'])
    net_connect = ConnectHandler(**HOST)

    config_commands = ['interface l0',
                       'ip address 1.1.1.1 255.255.255.0',
                       'do show ip interface br | i 1.1.1.1']

    output = net_connect.send_config_set(config_commands)
    print(output)
