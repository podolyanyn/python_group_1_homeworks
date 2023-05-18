def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = []
    for i in range(mid):
        left.append(array[i])

    right = []
    for i in range(mid, len(array)):
        right.append(array[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(array, left, right)


def merge(array, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array

print(merge_sort([10,20,0.5,3,1]))