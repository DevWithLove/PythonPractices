"""
78. Subsets
Medium
14.8K
215
Companies
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List

def get_subsets(nums:List[int]) -> List:
    subsets = [[]]
    for num in nums:
        n = []
        for s in subsets:
            new_set = s + [num]
            n.append(new_set)
        subsets += n
    return subsets
#print(get_subsets([1,2,3]))

class Solution:
    def solution(self,nums,ans,cur,index):
        if(index>len(nums)):
            return
        ans.append(cur[:])
        for i in range(index,len(nums)):
            if(nums[i] not in cur):
                cur.append(nums[i])
                self.solution(nums,ans,cur,i)
                cur.pop()
        return 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(nums,ans,cur,0)
        return ans
    
s = Solution()
print(s.subsets([1,2,3]))


