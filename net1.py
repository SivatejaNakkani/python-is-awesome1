from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        router = { 
        "device_type":"cisco_ios",
        "ip":"sandbox-iosxe-latest-1.cisco.com",
        "username":"developer",
        "password":"C1sco12345" 
        }
        netconnect = ConnectHandler(**router)
        
        print("Connecting to "+ IP)
        print('-'*80)
        output = netconnect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*80)

netconnect.disconnect()
