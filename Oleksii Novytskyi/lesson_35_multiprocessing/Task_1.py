import requests
import multiprocessing
import time
import threading
import concurrent.futures

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

def check_prime(i):
   if i == 2:
      return True
   if i < 2 or i % 2 == 0:
      return False
   for j in range(3, int(i ** 0.5) + 1, 2):
      if i % j == 0:
         return False
   return True

# print(check_prime(4350190374376723))




if __name__ == '__main__':



   start = time.time()
   with concurrent.futures.ProcessPoolExecutor(4) as executor:
      results = executor.map(check_prime, NUMBERS)

      # for result in results:
      #    print(result)

   stop = time.time() - start
   print(f'ProcessPoolExecutor done in {stop} sec')

   start1 = time.time()
   with concurrent.futures.ThreadPoolExecutor(4) as executor_:
      results_ = executor_.map(check_prime, NUMBERS)

      # for result in results_:
      #    print(result)

   stop1 = time.time() - start1
   print(f'ThreadPoolExecutor done in {stop1} sec')

   start2 = time.time()
   for i in NUMBERS:
      check_prime(i)
   stop2 = time.time() - start2
   print(f'Simple loop done in {stop2} sec')


