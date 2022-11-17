import socket

s = socket.socket()

print("Socket Successfully Created")

port =40674

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)

print("Socket is listening")

while True:
    c,addr = s.accept()
    print("Got connection from",addr)

    c.send(b"Thank you for connecting")

    c.close()