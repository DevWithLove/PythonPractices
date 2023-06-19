
"""
In Python, you use the double slash // operator to perform floor division. This // operator divides the first number by the second number and rounds the result down to the nearest integer (or whole number).
"""

# binary search is only work for sorted list
def binary_search(my_list, value):
    left = 0
    right = len(my_list) -1
    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] == value: 
            return mid
        if my_list[mid] < value:
            left = mid + 1
        elif my_list[mid] > value:
            right = mid - 1
    return -1


print(binary_search([1,2,3,4,5,6], 7))