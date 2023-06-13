# O(log n) в середньому пошук фібоначі призводить до виконання приблизно на 4% більшої кількості порівнянь,
# але його перевага в тому, що для обчислення індексів доступних елементів масиву потрібне лише додавання та віднімання

def fibonacci_search(arr, item):
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    pos = -1
    while fib > 1:
        i = min(pos + fib2, n - 1)
        if arr[i] == item:
            return i
        if arr[i] > item:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            pos = i
    if fib1 == 1 and pos < n - 1 and arr[pos + 1] == item:
        return pos + 1
    print('there is no an item in the array')
    return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
item = 12
print(fibonacci_search(arr, item))