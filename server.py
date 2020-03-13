import socket
# getting hostname name
host = socket.gethostname()
port = 1234

# binding address with host
server = socket.socket()
server.bind((host, port))

server.listen(2)

connection, address = server.accept()
print("connection from: " + str(address))

# decoding msg
while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    print("from connected user: " + str(data))
    connection.send("hello")
    connection.close()
