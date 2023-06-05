import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

def new_connection(client_socket):
    while True:
        data = client_socket.recv(1024)
        print(f"client's request: {data}")
        rez = b'The result for your request is...'
        if not data:
            break
        client_socket.sendall(rez)
    client_socket.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    while True:
        client_socket, address = s.accept()
        client_thread = threading.Thread(target=new_connection, args=(client_socket,))
        print(f"Accepted connection from {address[0]}:{address[1]}, thread: {client_thread.name}")
        client_thread.start()
        client_thread.join()


