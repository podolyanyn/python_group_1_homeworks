import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(num):
   if num < 2:
      return False
   for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
         return False
   return True

def filter_prime_numbers_threadpool(numbers):
   with ThreadPoolExecutor() as executor:
      return list(executor.map(is_prime, numbers))

def filter_prime_numbers_processpool(numbers):
   with ProcessPoolExecutor() as executor:
      return list(executor.map(is_prime, numbers))

if __name__ == '__main__':
   start = time.time()
   print(filter_prime_numbers_threadpool(NUMBERS))
   stop = time.time() - start
   print('ThreadPoolExecutor -', stop)
   start1 = time.time()
   print(filter_prime_numbers_processpool(NUMBERS))
   stop1 = time.time() - start
   print('ProcessPoolExecutor -', stop1)