"""
 Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
refer to https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List

# (O) = log(n)
class Solution:
    def getLeftPosition(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid-1 >= 0 and nums[mid-1] != target or mid == 0):
                    return mid
                right = mid-1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid+1

        return -1

    def getRightPosition(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums)-1):
                    return mid
                left = mid+1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid+1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftPosition(nums, target)
        right = self.getRightPosition(nums, target)

        return [left, right]
    
solution = Solution()

print(solution.searchRange([5,7,7,8,8,10], 8))
print(solution.searchRange([5,7,7,8,8,10], 6))
print(solution.searchRange([], 0))

#(O) = n
def find_element(nums: List[int], target: int) -> List[int]:
    try:
      first = nums.index(target)
      for i in range(first,len(nums)):
        if nums[i] == target:
            last = i
        else:
          return [first,last]
      return [first,first]
    except ValueError:
       return [-1, -1]


print(find_element([5,7,7,8,8,10], 8))
print(find_element([5,7,7,8,8,10], 6))
print(find_element([], 0))
