import asyncio
import socket

async def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)
    print(f"Disconnected from {client_address}")
    client_socket.close()

async def main():
    await asyncio.gather(handle_client(client_socket, client_address))

HOST = "127.0.0.1"
PORT = 65432

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.bind((HOST, PORT))
       s.listen()
       print(f"Server is listening on {HOST}:{PORT}")
       while True:
          client_socket, client_address = s.accept()
          asyncio.run(main())