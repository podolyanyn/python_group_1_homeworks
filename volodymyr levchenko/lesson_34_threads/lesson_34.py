# # Task 1
# import threading
# counter = 0
# rounds = 100000
# class Counter(threading.Thread):
#
#     def run(self):
#         global counter, rounds
#         for i in range(rounds):
#             counter += 1
#
# c1 = Counter()
# c2 = Counter()
#
# c1.start()
# c2.start()
#
# c1.join()
# c2.join()
#
# for _ in range(5):
#     print(f'iteration {_+1} : counter = {counter}')
#
# # Task 2
# import socket
# import threading
#
# def connection_handle(conn):
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break
#         conn.sendall(data)
#         print(f"received {data}")
#     conn.close()
#
#
# def echo_server():
#     host = '127.0.0.1'
#     port = 8080
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((host, port))
#     s.listen(5)
#     print('socket is listening')
#     while True:
#         conn, addr = s.accept()
#         print(f"connected by {addr}")
#         client_thread = threading.Thread(target=connection_handle, args=(conn,))
#         client_thread.start()
#
#
# echo_server()