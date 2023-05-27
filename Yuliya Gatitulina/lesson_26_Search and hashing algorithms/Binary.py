# O(log n)
def binary_search(arr, item, low, high):
    if low > high or item < arr[0] or item > arr[len(arr)-1]:
        print('there is no an item in the array')
        return -1
    mid = (low + high) // 2
    if arr[mid] == item:
        return mid
    if arr[mid] > item:
        return binary_search(arr, item, low, mid - 1)
    return binary_search(arr, item, mid + 1, high)


l1 = [1,2,3,4]
print(binary_search(l1, 2, 0, len(l1)-1))
