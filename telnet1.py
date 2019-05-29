# import getpass
import telnetlib

HOSTS = ["192.168.122.253", "192.168.122.160", "192.168.122.101"]
# user = input("Enter your remote account: ")
# password = getpass.getpass()

user = 'cisco'
password = 'cisco'

for HOST in HOSTS:
    print('Accessing {}'.format(HOST))
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show running-config | i ntp\n")
    tn.write(b"show running-config | i clock\n")
    tn.write(b"show running-config | i timestamps\n")

    tn.write(b"configure terminal\n")
    tn.write(b"ntp server 0.asia.pool.ntp.org prefer\n")
    tn.write(b"ntp server 1.asia.pool.ntp.org\n")

    tn.write(b"clock timezone IST 2 0\n")
    tn.write(b"clock summer-time IDT date March 29 2019 02:00 October 27 2019 02:00\n")
    tn.write(b"service timestamps debug datetime msec localtime show-timezone\n")
    tn.write(b"service timestamps log datetime msec localtime show-timezone\n")
    tn.write(b"end\n")

    tn.write(b"show running-config | i ntp\n")
    tn.write(b"show running-config | i clock\n")
    tn.write(b"show running-config | i timestamps\n")

    tn.write(b"show ntp packets\n")
    tn.write(b"show ntp associations\n")

    tn.write(b"exit\n")

    output = tn.read_all().decode('ascii')
    print(output)

    with open(HOST+'.txt', 'a') as out:
        out.write(output)