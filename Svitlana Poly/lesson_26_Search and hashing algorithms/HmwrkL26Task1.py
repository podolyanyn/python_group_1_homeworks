#Програма мінімум:

#Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.

def bin_search_rec(arr, target):
    arr = sorted(arr)
    mid = len(arr)//2
    
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        left = arr[:mid]
        result = bin_search_rec(left, target) #recursively calls itself on left half
        if result is not None:
            return result
    else:
        right = arr[mid+1:]
        result = bin_search_rec(right, target)
        if result is not None:
            return mid+1+ result

    return None #if element not found

arr = [8,2,5,3,7,4,6]
print(sorted(arr))
#[2, 3, 4, 5, 6, 7, 8]
target = 8

result = bin_search_rec(arr,target)
if result is not None:
    print(f'Element {target} found in list arr at index {result}')

else:
    print(f'Element {target} not found in the list arr')

#Element 8 found in list arr at index 6

#Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
#Визначте складність алгоритму та порівняйте його з бінарним пошуком.







