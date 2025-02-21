import json
from napalm import get_network_driver
import getpass

# Prompt for username and password
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# Load switch information from JSON file
with open('nwbptor.json')as f:
    switches_data = json.load(f)

# NAPALM driver for Cisco NX-OS
driver = get_network_driver('nxos')

# Iterate through switches and get serial numbers
for switch in switches_data['switches']:
    device = driver(
        hostname=switch['ip'],
        username=username,
        password=password
    )

    print(f"Connecting to {switch['name']} ({switch['ip']})...")
    try:
        device.open()
        facts = device.get_facts()
        serial_number = facts['serial_number']
        print(f"Switch Name: {switch['name']}, Serial Number: {serial_number}")
    except Exception as e:
        print(f"Error connecting to {switch['name']}: {str(e)}")
    finally:
        device.close()

print("Serial number retrieval complete.")