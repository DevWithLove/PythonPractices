"""
Given an arry of integers, return true if the following conditions are fulfilled

- length of the array is bigger than or equal to 3 
- There exists some index i such that:
  a[0]<a[1]<...a[i]
  a[i]>a[i+1]>...a[a.size - 1]

  In a nutshell: find if there is an increasing subarray flolowed by an decreasing subarray

  [3,5,5] => false
  [0,3,2,1] => true

"""
from typing import List

def isValidMountainArray(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False
    i = 1
    while i < len(nums) and nums[i] > nums[i-1]:
        i += 1
    
    if i == 1 or i == len(nums):
        return False
    while i < len(nums) and nums[i] < nums[i-1]:
        i += 1
    return i == len(nums)


print(isValidMountainArray([0,2,3,4,5,2,1,0]))
print(isValidMountainArray([0,2,2,4,5,2,1,0]))

