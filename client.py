# chat client side
import socket

# define constants to be used
# the IP address of the server
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# create a client side socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
client_socket.connect((HOST_IP, HOST_PORT))

# # receive the welcome message from the server
# welcome_message = client_socket.recv(BYTESIZE).decode(ENCODER)
# print(welcome_message)

# send/receive messages to/from the server
while True:
    # receive information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # quit if the message is "quit"
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("Ending the chat ...\n")
        break
    else:
        print("Server: " + message)
        message = input("Client: ")
        client_socket.send(message.encode(ENCODER))

# close the socket
client_socket.close()