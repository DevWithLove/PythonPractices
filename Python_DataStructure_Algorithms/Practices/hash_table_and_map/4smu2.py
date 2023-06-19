"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
"""
from typing import List

def sum42(l1:List[int], l2:List[int], l3:List[int], l4:List[int]) -> int:
   dict = {}
   total = 0
   for n in l1:
      for m in l2:
         sum = n + m
         if sum not in dict:
            dict[sum] = 0
         dict[sum] += 1
   for n in l3:
      for m in l4:
         sum = n + m 
         target = 0 - sum
         if target in dict:
            total += dict[target]
    
   return total


print(sum42([1,2], [-2,-1], [-1,2], [0,2]))
print(sum42([0], [0], [0], [0]))

