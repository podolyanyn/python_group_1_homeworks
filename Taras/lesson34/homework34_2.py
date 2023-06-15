import socket
import threading


def new_client(client_socket):
    while True:  # an endless cycle
        data = client_socket.recv(1024)  # receiving data from the client
        if not data:  # checking the availability of data
            break  # exit the loop if there is no data
        client_socket.send(data)  # sending data back to the client
    client_socket.close()  # closing the connection with the client


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a server socket
    server_socket.bind(('localhost', 12345))  # bind server socket to address and port
    server_socket.listen(3)  # listening for incoming connections
    print("The server is running. Tracking connections...")  # output message about starting the server
    while True:  # an endless cycle
        client_socket, address = server_socket.accept()  # waiting for a connection with the client
        print("Connected client at address:", address)  # output information about the connected client
        client_thread = threading.Thread(target=new_client, args=(client_socket,))  # create a new thread to handle the
        # client
        client_thread.start()  # start a thread to process the client


start_server()


