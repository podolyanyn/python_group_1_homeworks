import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024  # specifies the maximum number of bytes a server can receive from a client in a single message
msgFromServer = "Hello UDP Client"  # message will be sent from the server to the client
bytesToSend = str.encode(msgFromServer)  # converts the string into a byte representation that can be sent over the
# network
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((localIP, localPort))  # bind the socket to the specified IP address and port. This tells the server on which
# address and port to expect incoming connections
print("UDP server up and listening")  # output a message to the console to confirm that the server is running and
# listening for incoming connections
while (True):  # create an endless loop
    bytesAddressPair = sock.recvfrom(bufferSize)  # receive the data sent by the client
    message = bytesAddressPair[0]  # unpack the value of the variable. Here is a message from a client
    address = bytesAddressPair[1]  # here is the address of the client
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)  # format the variables to build a message from the information
    # received from the client about the message and the client's IP address.
    print(clientMsg)
    print(clientIP)
    sock.sendto(bytesToSend, address)  # send a response to the client














