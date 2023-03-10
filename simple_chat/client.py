from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8020))

message_bytes = client_socket.recv(1024)
message = message_bytes.decode('utf-8')
print(message)


