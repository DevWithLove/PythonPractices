"""
HT: Find Duplicates ( ** Interview Question)
find_duplicates()


Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).


Input:

A list of integers nums.


Output:

A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].



Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [2, 3]
Explanation: The numbers 2 and 3 appear more than once in the input array.
 
Input: nums = [1, 2, 3, 4, 5]
Output: []
Explanation: There are no duplicates in the input array, so the function returns an empty list [].
 
Input: nums = [3, 3, 3, 3, 3]
Output: [3]
Explanation: The number 3 appears more than once in the input array.
 
Input: nums = [-1, 0, 1, 0, -1, -1, 2, 2]
Output: [-1, 0, 2]
Explanation: The numbers -1, 0, and 2 appear more than once in the input array.
 
Input: nums = []
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].
"""


def find_duplicates(nums):
    num_counts = {}
    for num in nums:
        # add the number to the hash table or increment its count if it's already in the hash table
        num_counts[num] = num_counts.get(num, 0) + 1
    duplicates = [num for num, count in num_counts.items() if count > 1]
    return duplicates

# def find_duplicates(list):
#     duplicates = dict()
#     for i in list:
#         if i in duplicates:
#             duplicates[i] = True
#         else:
#             duplicates[i] = False
#     return [key for (key, value) in duplicates.items() if value == True]


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""