import socket

msgFromClient = "Hello UDP Server"  # create a variable and assign it the string value. This will be the message sent
# from the client to the server
bytesToSend = str.encode(msgFromClient)  # converts the string into a byte representation that can be sent over the
# network
serverAddressPort = ("127.0.0.1", 20001)  # create a variable assign it a tuple containing the IP address and the port
# number of the server
bufferSize = 1024  # specifies the maximum number of bytes the client can receive from the server in a single
# message
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)  # sends the message over the UDP socket to the specified
# server address and port
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])  # prepares the message to be printed.
print(msg)  # print the message from the server to the console. Displays the response received from the server







