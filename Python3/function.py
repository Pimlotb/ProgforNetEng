
def device_type(device):
    if device == '1800':
        return ("Its a Cisco Router")
    if device == '2900':
        return ("Its a Cisco Router")
    if device == '3750':
        return ("Its a Cisco Switch")
    if device == '3850':
        return ("Its a Cisco Switch")

whatdevice = input("Enter a device [1800,2900,3750,3850]:")
answer = device_type(whatdevice)

print(answer)