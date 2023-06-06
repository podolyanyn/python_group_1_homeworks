# binary_task
# def binary_search(arr, target, low, high):
#     if low > high:  # check if the lower bound is greater than the upper bound
#         return -1  # element not found
#     mid = (low + high) // 2  # calculate the middle index of the current sublist
#     if arr[mid] == target:  # check if the middle element is the target element
#         return mid  # element found
#     if arr[mid] > target:  # if the middle element is greater than the target, recursively search in the left half of
#         # the sublist
#         return binary_search(arr, target, low, mid - 1)
#     else:  # If the middle element is less than the target, recursively search in the right half of the sublist
#         return binary_search(arr, target, mid + 1, high)
#
#
# arr = [2, 3, 9, 10, 15, 18, 22, 25, 27]
# target = 18
# result = binary_search(arr, target, 0, len(arr) - 1)
# if result != -1:
#     print('Element index: ', result)
# else:
#     print('Element not found.')
# fibonacci_task
def fibonacci_search(arr, target):  # create a sequence of Fibonacci numbers reaching or exceeding the size of the list
    fib2 = 0  # n - 2 Fibonacci element
    fib1 = 1  # n - 1 Fibonacci element
    fib = fib1 + fib2  # n Fobonacci element
    while fib < len(arr):
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1  # shift
    while fib > 1:
        i = min(offset + fib2, len(arr) - 1)  # calculate the index of the element we are checking
        if arr[i] < target:  # if the element is smaller than the required one, move the left border
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:  # if the element is larger than the required one, move the right border
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i  # element found
    if fib1 and arr[offset + 1] == target:  # check the last element
        return offset + 1
    return -1  # element isn't in the list


arr = [1, 4, 6, 8, 13, 24, 35, 64, 90]
target = 13
result = fibonacci_search(arr, target)
if result != 1:
    print('Element index: ', result)
else:
    print('Element not found.')
# складність алгоритму O(log n)
