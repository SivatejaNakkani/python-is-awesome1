import os, ipaddress

os.system('cls')
while True:
    ip = input("Enter the ip Address: ")
    try:
        print(ipaddress.ip_address(ip))
        print('ip Valid')
    except:
        print('-',n*50)
        print('ip is not valid')
    finally:
        if ip == 'q':
            print("script finished")
            break