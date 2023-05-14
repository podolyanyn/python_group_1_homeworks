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

#Task2 
#Прочитати про Fibonacci search та імплементуйте його за допомогою Python.
#Визначте складність алгоритму та порівняйте його з бінарним пошуком.

def fibonacci_search(arr, x):

    

    fib2 = 0 # (n-2)th Fibonacci number

    fib1 = 1 # (n-1)th Fibonacci number

    fib = fib1 + fib2 # nth Fibonacci number

    

    # Find smallest Fibonacci number greater than or equal to length of array

    while fib < len(arr):

        fib2 = fib1

        fib1 = fib

        fib = fib1 + fib2

    

 

    offset = -1

    

    

    while fib > 1:

        

        i = min(offset + fib2, len(arr)-1)

        

        if arr[i] < x:

            fib = fib1

            fib1 = fib2

            fib2 = fib - fib1

            offset = i

        

        

        elif arr[i] > x:

            fib = fib2

            fib1 = fib1 - fib2

            fib2 = fib - fib1

        

        

        else:

            return i

    

   

    if arr[offset+1] == x:

        return offset+1

    else:

        return -1

#task2. a) Часова складність алгоритму пошуку Фібоначчі становить O(log n), де n - довжина вхідного масиву. Це пов'язано з тим, що алгоритм розбиває масив на все менші і менші підмасиви, кожен з яких можна обробити за O(1) часу, використовуючи порівняння та арифметичні операції з постійним часом.

Алгоритм пошуку Фібоначчі використовує послідовність Фібоначчі для визначення індексів елементів, що порівнюються, i кожне порівняння зменшує розмір простору пошуку приблизно в 1,6 рази (золотий перетин). Це означає, що кількість порівнянь, необхідних для пошуку цільового елемента, обмежена логарифмом довжини масиву, округленим до найближчого цілого числа.

У найгіршому випадку цільовий елемент відсутній у масиві, і алгоритм виконує повний перебір масиву, що вимагає O(log n) порівнянь. У кращому випадку цільовий елемент знаходиться за першим індексом, і алгоритм повертається після одного порівняння, що знову ж таки потребує O(log n) часу.

Таким чином, часова складність алгоритму пошуку Фібоначчі становить O(log n) як у найгіршому, так і в найкращому випадку. 

#task2. b Алгоритм пошуку за Фібоначчі - це алгоритм пошуку, який використовує послідовність Фібоначчі для розділення відсортованого масиву на менші підмасиви для виконання пошуку. Порівняльна складність пошуку за Фібоначчі становить O(log n), як і двійкового пошуку.

Однак, пошук за Фібоначчі має вищі накладні витрати, ніж бінарний пошук, через обчислення, необхідні для обчислення чисел Фібоначчі. На практиці бінарний пошук, як правило, швидший за пошук за Фібоначчі, оскільки він має менший постійний коефіцієнт і вимагає меншої кількості порівнянь.

Тому, хоча обидва алгоритми мають однакову порівняльну складність, бінарний пошук зазвичай швидший і частіше використовується на практиці.





