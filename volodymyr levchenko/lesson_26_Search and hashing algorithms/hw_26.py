"""
homework № 26
Search and hash algorithms
"""
# # Task 1
# def bin_search(array, a):
#     l, r = 0, len(array) - 1
#     m = (l+r)//2
#     if array[m] == a:
#         return m
#     elif array[m] > a:
#         return bin_search(array[:m], a)
#     else:
#         return m + 1 + bin_search(array[m+1:], a)
#
#
# some_array = [2, 5, 7, 8, 11, 13, 17, 19, 21, 25]
#
# print(bin_search(some_array, 21))
#
# # Fibonacci Search
# def fib_search(array, e):
#     n = len(array)
#     start = -1
#     if n == 0:
#         return -1
#     fib1, fib2 = 0, 1
#     fib3 = fib1 + fib2
#     while fib3 < n:
#         fib1, fib2 = fib2, fib3
#         fib3 = fib1 + fib2
#     while fib3 > 1:
#         i = min(start + fib2, n-1)
#
#         if array[i] < e:
#             fib3 = fib2
#             fib2 = fib1
#             fib1 = fib3 - fib2
#             start = i
#         elif array[i] > e:
#             fib3 = fib1
#             fib2 = fib2 - fib1
#             fib1 = fib3 - fib2
#         else:
#             return i
#
#     if fib2 == 1 and array[start + 1] == e:
#         return start + 1
#     else:
#         return -1
#
#
# some_array = [1, 13, 15, 17, 19, 21, 32, 42, 54]
# print(fib_search(some_array, 17))
