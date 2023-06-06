# # Task 1
# def bubblesort(list1):
#     start = 0
#     n = len(list1)
#     end = n - 1
#     swapped = True
#     while swapped:
#         swapped = False
#         for j in range(start, end):
#             if list1[j] > list1[j+1]:
#                 list1[j], list1[j+1] = list1[j+1], list1[j]
#                 swapped = True
#         if not swapped:
#             break
#
#         swapped = False
#
#         for j in range(end-1, start-1, -1):
#             if list1[j] > list1[j+1]:
#                 list1[j], list1[j+1] = list1[j+1], list1[j]
#                 swapped = True
#
#         start +=1
#         end -=1
#
#     return list1
#
# print(bubblesort([1, 5, 2, 10, 3]))
#
# # Task 2
# def merge_sort(unsorted_list):
#    if len(unsorted_list) <= 1:
#       return unsorted_list
#    middle = len(unsorted_list) // 2
#    left_list = []
#    right_list = []
#    for i in range(middle):
#       left_list.append(unsorted_list[i])
#    for j in range(middle, len(unsorted_list)):
#       right_list.append(unsorted_list[j])
#    left_list = merge_sort(left_list)
#    right_list = merge_sort(right_list)
#    return list(merge(left_list, right_list))
#
# # Merge the sorted halves
# def merge(left_half,right_half):
#    res = []
#    while len(left_half) != 0 and len(right_half) != 0:
#       if left_half[0] < right_half[0]:
#          res.append(left_half[0])
#          left_half.remove(left_half[0])
#       else:
#          res.append(right_half[0])
#          right_half.remove(right_half[0])
#    if len(left_half) == 0:
#       res = res + right_half
#    else:
#       res = res + left_half
#    return res
# unsorted_list = [64, 34, 25, 12, 22, 11, 90]
# print(merge_sort(unsorted_list))

