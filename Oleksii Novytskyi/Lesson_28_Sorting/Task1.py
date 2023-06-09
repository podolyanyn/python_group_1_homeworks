import timeit

# варіант 1 (але не зовсім по завданню :))
def bubble_sort(array):
    for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if j % 2 == 0:
                    if array[j] > array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
                else:
                    if array[len(array)-i-1] < array[j]:
                        array[len(array)-i-1], array[j] = array[j], array[len(array)-i-1]
    return array

print(bubble_sort([2,1,0,3,0.5]))

def bidirectional_bubble_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    swapped = True

    while swapped:
        swapped = False

        # ліво-право
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False

        # право-ліво
        right -= 1
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1

    return arr

print(bidirectional_bubble_sort([2,1,0,3,0.5]))
print(timeit.timeit(lambda: bidirectional_bubble_sort([2,1,0,3,0.5]), number=100000))
print(timeit.timeit(lambda: bubble_sort([2,1,0,3,0.5]), number=100000))

# на мою думку доречно використовувати такий метод при малих об'ємах даних.