def create_vlans(vlan_no,vlan_name):
    return{'vlan': vlan_no, 'name': vlan_name}

vlan_no = input("Enter VLAN number:")
vlan_name = input("Enter VLAN name:")

answer = create_vlans(vlan_no,vlan_name)

print(answer)