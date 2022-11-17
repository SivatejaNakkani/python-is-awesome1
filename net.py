from netmiko import ConnectHandler

CSR = {
        "device_type":"cisco_ios",
		"ip":"sandbox-iosxe-latest-1.cisco.com",
		"username":"developer",
		"password":"C1sco12345"
}

net_connect = ConnectHandler(**CSR)


#output = net_connect.send_command('show ip int brief')
#output_clock = net_connect.send_command('show clock')
#output_routes = net_connect.send_command('show ip ro')
output_runconfig = net_connect.send_command('show run')

print(output_runconfig)
#print(output_clock)

#print(output)

net_connect.disconnect()