from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8020))

server_socket.listen()
print("Server started on port 8020")

message = str.encode("Welcome!")
while True:
    conn, addr = server_socket.accept()
    print(addr, conn)
    conn.send(message)




