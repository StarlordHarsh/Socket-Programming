import socket

protocol ='tcp'
for port in [80, 25]:
    print("Port: %s -> Service nsmr: %s" %(port, socket.getservbyport(port, protocol)))

print("Port: %s -> service name: %s"%(53, socket.getservbyport(53, 'udp')))