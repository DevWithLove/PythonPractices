"""
136. Single Number
Easy
14.1K
547
Companies
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

hint:
we have 3 numbers, a, b, c
total (2a+2b+2c) => 2(a+b+c)
if c is single number
total (2a+2b+c)

Better soultion:
number presentation in binary:
  8 4 2 1
  0 1 0 1 
  = 8*0 + 4*1 + 2*0 + 1*1 = 5
  8 4 2 1
  1 0 1 1 
  = 8*1 + 4*0 + 2*1 + 1*1 = 11

  we can manipulate these bits individually to give us different numbers using bit manipulation operations like 
  or operation, and operation, xor operation
  XOR compares two inputs bits and generates one output bit in following rule:
    1. if the bits are the same, result is 0
    2. if the bits are different, the result is 1

    1 0 1 1
    1 0 1 1
    xor => 0 0 0 0 
    0 0 0 0
    0 0 0 1
    xor => 0 0 0 1

"""

from typing import List

# time O(n) space O(n)
def findSingleNumber(nums:List[int]) -> int:
    numSet = set(nums)
    intend_total = sum(numSet)*2
    total = sum(nums)
    return intend_total - total
# time O(n), space O(1)
def findSingleNumber2(nums:List[int]) -> int:
    result = 0
    for n in nums:
      result = result ^ n
    return result

print(findSingleNumber([2,2,1]))
print(findSingleNumber([4,1,2,1,2]))
print(findSingleNumber([1]))

print(findSingleNumber2([2,2,1]))
print(findSingleNumber2([4,1,2,1,2]))
print(findSingleNumber2([1]))
