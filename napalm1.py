import json
from napalm import get_network_driver

driver = get_network_driver('ios')
ios = driver('192.168.30.139', 'cisco', 'cisco')
ios.open()

print('Accessing 192.168.30.139')
ios.load_merge_candidate(filename='hostname.cfg')
ios.commit_config()
ios.close()