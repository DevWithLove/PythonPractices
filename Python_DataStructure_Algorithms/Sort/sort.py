

def bubble_sort(my_list):
    for i in range(len(my_list)-1 , 0, -1):
        print(f"i = {i}")
        for j in range(i):
            print(f"j = {j}")
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1,len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i: 
            temp = my_list[min_index]
            my_list[min_index] = my_list[i]
            my_list[i] = temp
    return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1: 
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


# print(insertion_sort([4,2,6,5,1,3])) 

# print(selection_sort([4,2,6,5,1,3]))   

# print(bubble_sort([4,2,6,5,1,3]))

# merge sort (n log n)
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

def merge_sort(my_list):
     if len(my_list) == 1: 
         return my_list
      
     mid_index = int(len(my_list)/2)
     left = merge_sort(my_list[:mid_index])
     right = merge_sort(my_list[mid_index:]) 

     return merge(left ,right)
         
# list1 = [3,1,4,2]
# merge_sorted = merge_sort(list1)
# print(list1) 
# print(merge_sorted)
# print(merge([1,3,7,8], [2,4,5,6]))

# Quick sort 
def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list
    

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)


my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)

