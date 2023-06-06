
array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def bin_serch(array, elem):

    try:
        mid = len(array) // 2
        if array[mid] == elem:
            return mid
        elif array[mid] > elem:
            res = bin_serch(array[:mid], elem)
            return res
        elif array[mid] < elem:
            res = bin_serch(array[mid:], elem)
            return res + mid
    except: RecursionError
    return 'no such element'

print(bin_serch(array_1, 1))


def fibonacci_search(array, target):
    size = len(array)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, size - 1)
        if array[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if f1 and (array[size - 1] == target):
        return size - 1
    return 'no such element'

print(fibonacci_search(array_1, 10))