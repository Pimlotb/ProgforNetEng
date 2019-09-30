#!/usr/bin/env python3.7
# executing commands
# upgrading devices
# rebooting devices
# saving / backup
# sudo pip install pyntc
# pip install cryptography

import json
from pynct import ntc_device as NTC

# CREATE DEVICE OBJECT FOR A IOS DEVICE
iosvl2 = NTC(host='192.168.122.75',username='blah',password='blah',device_type='cisco_nxos_nxapi')
iosvl2.open()

ios_output = iosvl2.facts
print (json.dumps(ios_output, indent=4))

iosvl2.config_list(['hostname s1_python','router ospf 1','network 0.0.0.0 255.255.255.255 area 0'])

# retrieve running config

ios_run = iosvl2.running_config
print (ios_run)

# Backup running config to a file
HOST = '192.168.22.75'
savedoutput = open('switch' + HOST, 'w')
savedoutput.write(ios_run)
savedoutput.close

# pyntc makes it easier
ios_run = iosvl2.backup_running_config('iosvl2-1.cfg')

