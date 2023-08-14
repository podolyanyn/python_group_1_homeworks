# asyncio виконується швидше за multiprocessing,
# чому - не знаю, мені здавалося, що повинно бути навпаки
# при подібних арифметичних обчисленнях
import time
import asyncio
import concurrent.futures

digits_list = [x for x in range(1, 11)]

async def fib(n):
    f1, f2 = 0, 1
    if n == 1: return f1
    if n == 2: return f2
    for i in range(3, n + 1):
        fib = f1 + f2
        f1 = f2
        f2 = fib
    return fib

async def fact(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

async def sq(n):
    return n * n

async def cub(n):
    return n ** 3

async def main():
    fibonacci_list = []
    factorial_list = []
    square_list = []
    cube_list = []
    for i in digits_list:
        fibonacci, factorial, square, cube = await asyncio.gather(fib(i), fact(i), sq(i), cub(i))
        fibonacci_list.append(fibonacci)
        factorial_list.append(factorial)
        square_list.append(square)
        cube_list.append(cube)
    print(f'fibonacci list: {fibonacci_list}')
    print(f'factorial list: {factorial_list}')
    print(f'square list: {square_list}')
    print(f'cube list: {cube_list}')

def fibonacci(n):
    f1, f2 = 0, 1
    if n == 1: return f1
    if n == 2: return f2
    for i in range(3, n + 1):
        fib = f1 + f2
        f1 = f2
        f2 = fib
    return fib

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def square(n):
    return n * n

def cube(n):
    return n ** 3

if __name__ == '__main__':

    start1 = time.time()
    asyncio.run(main())
    async_time = time.time() - start1
    print(f'async time {async_time}')

    start2 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print(f'fibonacci list: {list(executor.map(fibonacci, digits_list))}')
        print(f'factorial list: {list(executor.map(factorial, digits_list))}')
        print(f'square list: {list(executor.map(square, digits_list))}')
        print(f'cube list: {list(executor.map(cube, digits_list))}')
    process_time = time.time() - start2
    print(f'multiprocessing time {process_time}')

