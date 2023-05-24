# доречно для невеликої кількості данних
def bubble_sort(list):
    n = len(list)
    left = 0
    right = n - 1
    while left < right:
        # Прохід "вгору"
        for i in range(left, right):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        right -= 1

        # Прохід "вниз"
        for i in range(right, left, -1):
            if list[i] < list[i-1]:
                list[i], list[i-1] = list[i-1], list[i]
        left += 1

    return list

# test_list = [7,2,9,4,1]
# bubble_sort(test_list)
# print(test_list)


def merge(left, right):
    res = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res

# left = [3, 5, 8]
# right = [1, 2, 7]
# merged = merge(left, right)
# print(merged)
