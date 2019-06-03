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

    with open('netmiko1.cfg') as f:
        lines = f.read().splitlines()
    # print(lines)
    config_commands = lines

    output = net_connect.send_config_set(config_commands, delay_factor=4)
    print(output)
