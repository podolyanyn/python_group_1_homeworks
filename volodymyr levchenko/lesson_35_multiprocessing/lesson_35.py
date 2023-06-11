# import concurrent.futures
# from time import time as t
#
#
# def is_prime_checker(val):
#    if val < 2:
#       return False
#    for i in range(2, int(val**0.5) + 1):
#       if (val % i) == 0:
#          return False
#    return True
#
#
# def thread_pool_executor(numbers):
#    with concurrent.futures.ThreadPoolExecutor() as executor:
#       filtered = executor.map(is_prime_checker, numbers)
#    return list(filtered)
#
#
# def process_pool_executor(numbers):
#    with concurrent.futures.ProcessPoolExecutor() as executor:
#       filtered = executor.map(is_prime_checker, numbers)
#    return list(filtered)
#
#
# if __name__ == '__main__':
#    numbers = [
#       2,  # prime
#       1099726899285419,
#       1570341764013157,  # prime
#       1637027521802551,  # prime
#       1880450821379411,  # prime
#       1893530391196711,  # prime
#       2447109360961063,  # prime
#       3,  # prime
#       2772290760589219,  # prime
#       3033700317376073,  # prime
#       4350190374376723,
#       4350190491008389,  # prime
#       4350190491008390,
#       4350222956688319,
#       2447120421950803,
#       5,  # prime
#    ]
#    # # thread pool executor end - start = 32.82
#    # start = t()
#    # results_thread = thread_pool_executor(numbers)
#    # end = t()
#    # print(end-start)
#    # print(results_thread)
#    # # process pool executor end - start = 7.45
#    # start = t()
#    # results_process = process_pool_executor(numbers)
#    # end = t()
#    # print(end-start)
#    # print(results_process)
#
# Task 3
import socket
import multiprocessing

def connection_handle(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
        print(f"received {data}")
    conn.close()


def echo_server():
    host = '127.0.0.1'
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print('socket is listening')

    while True:
        conn, addr = s.accept()
        print(f"connected by {addr}")
        process = multiprocessing.Process(target=connection_handle, args=(conn,))
        process.start()


if __name__ == '__main__':
    echo_server()