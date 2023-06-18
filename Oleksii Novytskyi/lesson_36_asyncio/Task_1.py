'''В цьому прикладі мультипроцесорний варіант програє, на мою думку чурез затрати часу на створення процесів'''


# import asyncio
# import time
#
# my_list = [i for i in range(1, 11)]
#
#
# async def fib(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         # print(f'the fib of {n} = {0}')
#         return 0
#     elif n == 1:
#         # print(f'the fib of {n} = {b}')
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         # print(f'the fib of {n} = {b}')
#         return b
#
#
# async def sqrt(n):
#     # print(f'the sqrt of {n} = {n*n}')
#     return n*n
#
#
# async def cube(n):
#     # print(f'the cube of {n} = {n*n*n}')
#     return n*n*n
#
#
# async def factorial(n):
#     f = 1
#     for i in range(2, n + 1):
#         # print(f"Compute factorial({i})...")
#         f *= i
#     # print(f'the factorial of {n} = {f}')
#     return f
#
#
# async def main():
#     _fib = []
#     _sqrt = []
#     _cube = []
#     _factorial = []
#     for i in my_list:
#         a, b, c, d = await asyncio.gather(fib(i), sqrt(i), cube(i), factorial(i))
#         _fib.append(a)
#         _sqrt.append(b)
#         _cube.append(c)
#         _factorial.append(d)
#     print(f'the fib list: {_fib}')
#     print(f'the sqrt list: {_sqrt}')
#     print(f'the cube list: {_cube}')
#     print(f'the factorial list: {_factorial}')
#
#
# start = time.time()
# asyncio.run(main())
# rez = time.time() - start
# print(f'the async version spends {rez} seconds')

#

import time
import concurrent.futures

my_list1 = [i for i in range(1, 11)]

def _fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        # print(f'the fib of {n} = {0}')
        return 0
    elif n == 1:
        # print(f'the fib of {n} = {b}')
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        # print(f'the fib of {n} = {b}')
        return b


def _sqrt(n):
    # print(f'the sqrt of {n} = {n*n}')
    return n*n


def _cube(n):
    # print(f'the cube of {n} = {n*n*n}')
    return n*n*n


def _factorial(n):
    f = 1
    for i in range(2, n + 1):
        # print(f"Compute factorial({i})...")
        f *= i
    # print(f'the factorial of {n} = {f}')
    return f


if __name__ == '__main__':
    start1 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print(f'the fib list: {list(executor.map(_fib, my_list1))}')
        print(f'the sqrt list: {list(executor.map(_sqrt, my_list1))}')
        print(f'the fib list: {list(executor.map(_cube, my_list1))}')
        print(f'the fib list: {list(executor.map(_factorial, my_list1))}')
    rez1 = time.time() - start1
    print(f'the multiprocessing version spends {rez1} seconds')








