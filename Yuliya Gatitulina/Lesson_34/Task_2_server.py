import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    print(f"Disconnected from {client_address}")
    client_socket.close()

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
     s.bind((HOST, PORT))
     s.listen()
     print(f"Server is listening on {HOST}:{PORT}")
     while True:
        client_socket, client_address = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
        client_thread.join()



