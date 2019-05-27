import json
from napalm import get_network_driver

driver = get_network_driver('ios')
ios = driver('192.168.30.139', 'cisco', 'cisco')
ios.open()
ios_output = ios.get_facts()
print(json.dumps(ios_output, indent=4))