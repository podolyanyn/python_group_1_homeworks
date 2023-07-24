import socket
from threading import Thread
SERVER_HOST = 'localhost' # '0.0.0.0', '127.0.0.1'
SERVER_PORT = 5678
client_connections = {}  # {connection:['admin', 'room'], connection_1:['sys', 'default']}
rooms = {}   # {room_name:password}
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # try experiments !
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(5)
print(f'Server ready on {SERVER_HOST}:{SERVER_PORT}')
def listen_for_message(connection):
   while True:
        try:
            message = connection.recv(1024).decode()
            if len(message.split()) == 3:
                command, current_room_name, password = message.split()
            else:
                command, current_room_name, password = message, client_connections[connection][1], None
        except Exception as ex:
            print(f'Exception: {ex}')
            # continue
        else:
            if command == '/list':
                connection.send(str(rooms.keys()).encode())
            elif command == '/create':
                rooms[current_room_name] = password
                client_connections[connection] = ['admin', current_room_name]
                connection.send(f'Reconnect to {current_room_name}'.encode())
            elif command == '/join':
                if rooms.get(current_room_name) == password:
                    client_connections[connection] = ['user', current_room_name]
                    connection.send(f'You are in {current_room_name}'.encode())
                else:
                    connection.send(f'Wrong room name  or password'.encode())
            elif command == '/rename':
                if client_connections[connection] == ['admin', current_room_name]:
                    rooms[password] = rooms[current_room_name]
                    del rooms[current_room_name]
                    client_connections[connection][1] = password
                    connection.send(f'{current_room_name} rename to {password}'.encode())
                else:
                    connection.send(f'You are not admin'.encode())
            elif command == '/exit':
                client_connections[connection] = ['sys', 'default']
                connection.send(f'Logout from {current_room_name}'.encode())
            else:
                room_client_connections = dict(filter(lambda x: current_room_name == x[1][1], client_connections.items()))
                for conn in room_client_connections:
                    conn.send(message.encode())  # change after (send without me)
while True:
    connection, client_address = sock.accept()
    print(f'connected from client address: {client_address}')
    client_connections[connection] = ['sys', 'default']
    task = Thread(target=listen_for_message, args=(connection,), daemon=True)
    task.start()