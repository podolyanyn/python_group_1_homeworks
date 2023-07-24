def binary_recursion(l, value):
    if value not in l:
        return 'Not found'
    high = len(l)-1
    low = 0
    mid = (high+low)//2
    if l[mid] > value:
        l1 = l[:mid-1]
        return binary_recursion(l1, value)
    elif l[mid] < value:
        l1 = l[mid+1:high]
        return binary_recursion(l1, value)
    else:
        return mid


def fibSearch(l, x):
    n = len(l)
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1

    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1

    offset = -1

    while (fib > 1):
        i = min(offset + fib2, n - 1)
        if (l[i] < x):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif (l[i] > x):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if (fib1 and l[n - 1] == x):
        return n - 1

    return 'Not found'

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_recursion(list1, 5))
print(fibSearch(list1, 5))