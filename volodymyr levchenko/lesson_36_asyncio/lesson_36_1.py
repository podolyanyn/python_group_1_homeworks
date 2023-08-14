# # task 1
# import asyncio
#
#
# async def calculate_fibonacci(n):
#     if n <= 1:
#         return n
#     return await calculate_fibonacci(n - 1) + await calculate_fibonacci(n - 2)
#
#
# async def calculate_factorial(n):
#     if n == 0:
#         return 1
#     return n * await calculate_factorial(n - 1)
#
#
# async def calculate_squares(n):
#     return n * n
#
#
# async def calculate_cubic(n):
#     return n * n * n
#
#
# async def main():
#     tasks = [calculate_fibonacci(n) for n in range(1, 11)]
#     fib_results = await asyncio.gather(*tasks)
#
#     tasks = [calculate_factorial(n) for n in range(1, 11)]
#     fact_results = await asyncio.gather(*tasks)
#
#     tasks = [calculate_squares(n) for n in range(1, 11)]
#     square_results = await asyncio.gather(*tasks)
#
#     tasks = [calculate_cubic(n) for n in range(1, 11)]
#     cubic_results = await asyncio.gather(*tasks)
#
#     return fib_results, fact_results, square_results, cubic_results
#
#
# if __name__ == "__main__":
#     import time
#
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     fib_results, fact_results, square_results, cubic_results = loop.run_until_complete(main())
#     end = time.time()
#
#     print("fib:", fib_results)
#     print("factorial:", fact_results)
#     print("squares:", square_results)
#     print("cubic:", cubic_results)
#
#     print("async time:", end - start)
# # async time: 0.00099945068359375
#
#
# import multiprocessing
#
#
# def calculate_fibonacci(n):
#     if n <= 1:
#         return n
#     return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
#
#
# def calculate_factorial(n):
#     if n == 0:
#         return 1
#     return n * calculate_factorial(n - 1)
#
#
# def calculate_squares(n):
#     return n * n
#
#
# def calculate_cubic(n):
#     return n * n * n
#
#
# def main():
#     pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
#
#     fib_results = pool.map(calculate_fibonacci, range(1, 11))
#     fact_results = pool.map(calculate_factorial, range(1, 11))
#     square_results = pool.map(calculate_squares, range(1, 11))
#     cubic_results = pool.map(calculate_cubic, range(1, 11))
#
#     pool.close()
#     pool.join()
#
#     return fib_results, fact_results, square_results, cubic_results
#
#
# if __name__ == "__main__":
#     import time
#
#     start = time.time()
#     fib_results, fact_results, square_results, cubic_results = main()
#     end = time.time()
#
#     print("fib:", fib_results)
#     print("factorial:", fact_results)
#     print("squares:", square_results)
#     print("cubic:", cubic_results)
#
#     print("multiprocessing time:", end - start)
# # multiprocessing time: 0.18992877006530762
#


