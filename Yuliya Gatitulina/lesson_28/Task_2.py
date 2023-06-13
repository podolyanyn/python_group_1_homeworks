def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = []
    for i in range(mid):
        left.append(arr[i])
    right = []
    for i in range(mid, len(arr)):
        right.append(arr[i])
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

print(merge_sort([8,4,2,5,6,9,1]))