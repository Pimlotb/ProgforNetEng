from netmiko import ConnectHandler


def netmiko_connection(ip):
    return{
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'david',
        'password': 'cisco',
    }

iplist = [ '192.168.10.1','192.168.10.2','192.168.10.4']

for ip in iplist:
    ios=netmiko_connection(ip)

print (ios)