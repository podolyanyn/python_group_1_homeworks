import socket
from threading import Thread
SERVER_HOST = 'localhost' # '0.0.0.0', '127.0.0.1'
SERVER_PORT = 5678
sock = socket.socket()
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # try experiments !
print(f'Try connect on {SERVER_HOST}, {SERVER_PORT}')
sock.connect((SERVER_HOST, SERVER_PORT))
print('conected !')
name = input('Enter your name: ')
def listen_server():
    while True:
        message = sock.recv(1024).decode()
        print(message)
task = Thread(target=listen_server, daemon=True)
task.start()
commands = """ All available commands:
/list : Get all rooms
/create room_name password : Create new room
/join  room_name password : Join to existing room
/rename room_name new_room_name : Rename room by administrator
/exit : Exit from current room
/close : Close program
"""
print(commands)
while True:
    message = input()
    if message.split()[0] in ['/list', '/create', '/join','/rename','/exit']:
        sock.send(message.encode())
    elif message.split()[0] == '/close':
        sock.close()
        break
    else:
        message_for_send = f'{name}: {message}'
        sock.send(message_for_send.encode())