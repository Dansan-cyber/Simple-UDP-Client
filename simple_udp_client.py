import socket

target_host = "127.0.01"
target_port = 80

#creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC",(target_host, target_port))

#receive some data
data, addr = client.recvfrom(4096)

print response
