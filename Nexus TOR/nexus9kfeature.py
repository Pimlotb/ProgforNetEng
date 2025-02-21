import json
from napalm import get_network_driver
import getpass

# Prompt for username and password
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# Load switch information from JSON file
with open('nwbptor.json') as f:
    switches_data = json.load(f)

# NAPALM driver for Cisco NX-OS
driver = get_network_driver('nxos')

# Command to enable NX-API
enable_nxapi_command = 'feature nxapi'

# Iterate through switches and enable NX-API
for switch in switches_data['switches']:
    device = driver(
        hostname=switch['ip'],
        username=username,
        password=password
    )

    print(f"Connecting to {switch['name']} ({switch['ip']})...")
    try:
        device.open()
        device.load_merge_candidate(config=enable_nxapi_command)
        diff = device.compare_config()
        if diff:
            print(f"Enabling NX-API on {switch['name']}...")
            device.commit_config()
            print(f"NX-API enabled on {switch['name']}")
        else:
            print(f"NX-API is already enabled on {switch['name']}")
    except Exception as e:
        print(f"Error connecting to {switch['name']}: {str(e)}")
    finally:
        device.close()

print("NX-API enablement process complete.")