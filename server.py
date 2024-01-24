# chat server side
import socket

# define constants to be used
# the IP address of the server
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# create a server side socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a tuple (IP address, port address)
server_socket.bind((HOST_IP, HOST_PORT))
# listen for connections
server_socket.listen()

# accept incoming connections and let them know that they are connected
print('Server is running and listening ...\n')
client_socket, client_address = server_socket.accept()
client_socket.send('You are connected to the server ...\n'.encode(ENCODER))

# send/receive messages to/from the client
while True:
    # receive information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # quit if the message is "quit"
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("Ending the chat ...\n")
        break
    else:
        print("Client: " + message)
        message = input("Server: ")
        client_socket.send(message.encode(ENCODER))