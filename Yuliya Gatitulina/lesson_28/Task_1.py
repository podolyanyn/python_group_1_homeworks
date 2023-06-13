#The bidirectional bubble sort can be appropriate in certain circumstances when you have
# specific knowledge about the data you are sorting. It can be useful when the data is
# partially sorted or when there are multiple values that need to be placed at the correct
# positions at the beginning and end of the list.

def bidirectional_bubble_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr

print(bidirectional_bubble_sort([3,7,2,4,5,1,6]))