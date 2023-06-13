import random


# task_1
def bubble_sort(arr):
    n = len(arr)
    is_sorted = False  # initialize the "is_sorted" variable to "False" to start sorting
    while not is_sorted:  # execute the loop until the list is sorted
        is_sorted = True  # assume the list is already sorted (before each iteration)
        # pass "up" (from start to end)
        for i in range(n - 1):  # go through the list from index 0 to n-1
            if arr[i] > arr[i + 1]:  # if the current element is larger than the next one, swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False  # indicate that the list is not yet sorted
        if is_sorted:  # if the list is already sorted, exit the loop
            break
        is_sorted = True  # again assume the list is already sorted (before each iteration)
        # pass "down" (from end to beginning)
        for i in range(n - 2, -1, -1):  # go through the list from index n-2 to 0 (inclusive), with a step of -1
            if arr[i] > arr[i + 1]:  # if the current element is larger than the next one, swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False  # indicate that the list is not yet sorted
    return arr  # return the sorted list


my_list = [5, 2, 8, 12, 3, 7, 1, 9]
sorted_list = bubble_sort(my_list)
print("Bubble sort: ", sorted_list)
# даний підхід корисний в ситуаціях, коли ми маємо список, в якому невелика кількість невпорядкованих елементів
# розташовані в близькій відстані один від одного, а решта вже більш-менш впорядкована. У таких випадках альтернативний
# прохід "вниз" дозволяє швидше переміщувати ці невпорядковані елементи назад до їх правильних місць, що дозволяє
# зменшити кількість ітерацій, необхідних для завершення сортування.


# task_2
def merge_sort(arr):
    if len(arr) <= 1:  # if the list has 0 or 1 element, it is already sorted
        return arr
    mid = len(arr) // 2  # find the middle of the list
    left = [0] * mid  # create two new lists of pre-initialized size to split "arr" list into two halves.
    right = [0] * (len(arr) - mid)
    for i in range(mid):  # copy the first half of "arr" list to the "left" list
        left[i] = arr[i]
    for i in range(mid, len(arr)):  # copy the second half of "arr" list to the "right" list
        right[i - mid] = arr[i]
    merge_sort(left)  # recursively call the "merge_sort" for "left" and "right" lists to sort them
    merge_sort(right)
    i = j = k = 0  # initialize the variables for merging the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # compare elements from the left and right halves of the list
            arr[k] = left[i]  # place a smaller element in the original list
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):  # if there are any elements left in the "left", add them to "arr" using counters i and k
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):  # if there are any elements left in the "right", add them to "arr" using counters j and k
        arr[k] = right[j]
        j += 1
        k += 1
    return arr  # return the sorted list


mylist = [6, 4, 10, 12, 15, 20, 1, 9]
slist = merge_sort(mylist)
print("Merge sort: ", slist)


# task_3
def quick_sort(arr, partition_limit):
    if len(arr) <= partition_limit:  # if the size of the list is less than or equal to the separation limit, then
        # insertion sort is used to sort small lists
        insertion_sort(arr)
    else:
        if len(arr) > 1:  # if the size of the list is greater than 1, "pivot" element is chosen randomly
            pivot = arr[random.randint(0, len(arr) - 1)]
            smaller = [x for x in arr if x < pivot]  # lists "smaller", "equal", and "larger" are created to store
            # elements that are less than, equal to, and greater than the reference element, respectively
            equal = [x for x in arr if x == pivot]
            larger = [x for x in arr if x > pivot]
            quick_sort(smaller, partition_limit)  # quicksort is called recursively for the "smaller" and "larger" with
            # the same separation boundary
            quick_sort(larger, partition_limit)
            arr[:] = smaller + equal + larger  # "arr" is updated, combining "smaller", "equal" and "larger" in the
            # correct order


def insertion_sort(arr):
    for i in range(1, len(arr)):  # loop iterates over the elements of "arr" list starting from index 1
        key = arr[i]  # "key" stores the value of the current element
        j = i - 1  # "j" defines the index of the previous element
        while j >= 0 and arr[j] > key:  # loop is executed until "j" is greater than or equal to 0 and the previous
            # element is greater than "key"
            arr[j + 1] = arr[j]  # all elements greater than "key" are shifted to the right by one position
            j -= 1
        arr[j + 1] = key  # after the loop completes, "key" element is inserted into the correct position in the sorted
        # part of the list


random_list = random.sample(range(1, 101), 10)
print('Our random list: ', random_list)
quick_sort(random_list, 5)
print("Sorted list: ", random_list)






