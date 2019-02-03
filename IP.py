import socket

remote_host = input("Enter a site name to find ots IP-")
try:
    print("IP address of %s: %s" % (remote_host, socket.gethostbyname(remote_host)))
except socket.error as err_msg:
    print("%s: %s" % (remote_host, err_msg))
