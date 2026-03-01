##
# DAY ONE
# Sliding Window（Microsoft 高频核心 Pattern）。
# Sliding Window Pattern:
# 右扩张，左收缩，更新结果
#
# 
# left = 0

# for right in range(len(nums)):

#     # expand window

#     while window is invalid:
#         left += 1

#     update result
#
#####

### Longest Substring Without Repeating Characters
# https://www.jointaro.com/interviews/questions/longest-substring-without-repeating-characters/?company=microsoft
# Medium, Very likely 

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         left = 0
#         longest = 0
#         chars_in_string = {}

#         for right , char in enumerate(s):

#             #因为如果字符上次出现的位置在窗口外（< left），那它并不算“窗口内重复”，不能把 left 往回拉。
#             #比如窗口已经从 left=5 开始了，char 上次出现在 2，那根本无关。
#             if char in chars_in_string and chars_in_string[char] >= left:
#                 print(f"{s[left:right]} , {char}, {left}")
#                 left = chars_in_string[char] + 1
            
#             chars_in_string[char] = right
    
#             longest = max(longest, right - left + 1)

#         return longest
    
# #print(Solution().lengthOfLongestSubstring("bbbbb"))
# #print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("ohomm")) 

### Minimum Size Subarray Sum
# https://www.jointaro.com/interviews/questions/minimum-size-subarray-sum/?company=microsoft
## mediium , not likely

# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         minimum_window_size = float('inf')
#         left = 0
#         window_sum = 0
        
#         for right in range(len(nums)):
#             window_sum += nums[right]

#             # shrink the windows from the left unil win sum is smaller than target
#             while window_sum >= target:
#                 minimum_window_size = min(minimum_window_size, right - left +1)
#                 # reduce sum as we shrink the window
#                 window_sum -= nums[left]
#                 left += 1
#         return 0 if minimum_window_size == float('inf') else minimum_window_size

# print(Solution().minSubArrayLen(7, [2,3,1,2,4,3])) 
# print(Solution().minSubArrayLen(4, [1,4,4])) 
# print(Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1])) 

### Longest Repeating Character Replacement（
# https://www.jointaro.com/interviews/questions/longest-repeating-character-replacement/?company=microsoft
## mediium , not likely

# ① r - l + 1

# 窗口长度

# ② maxCount

# 窗口里“出现次数最多的那个字符”的次数

# 那 (窗口长度 - maxCount) 是什么？

# 👉 它表示：

# 当前窗口里，有多少个字符 不是那个最多的字符

# 也就是：

# 要把整个窗口变成“同一个字符”，我们至少要替换多少个字符

# 三、那为什么是 > k？

# 题目说：

# 最多只能替换 k 次

# 如果：

# 需要替换次数 <= k

# 那这个窗口是合法的。

# 如果：

# 需要替换次数 > k

# 说明窗口太大了 ❌
# 我们必须缩小窗口（移动左指针）。

# class Solution(object):
#     def characterReplacement(self, s, k):
#         count  = { }
#         left = 0
#         max_freq = 0
#         longest = 0

#         for right, ch in enumerate(s):
#             count[ch] = count.get(ch, 0) + 1
#             max_freq = max(max_freq, count[ch])
#             # if we need more than k replacements, shrink from left
#             while (right - left + 1) - max_freq > k:
#                 left_ch = s[left]
#                 count[left_ch] -= 1
#                 left += 1
#             longest = max(longest, right - left +1)

#         return longest
    

# print(Solution().characterReplacement("ABABBBB", 1))

#########################################################3
##
# DAY TWO
# Hashmap Pattern
# 
#

#################################
##  Two Sum
## https://www.jointaro.com/interviews/questions/two-sum/?company=microsoft
## easy , most asked
###########

# class Solution(object):
#     def twoSum(self, nums, target):
#        lookup = { }

#        for index, k in enumerate(nums):
#            if target - k in lookup:
#                return [lookup[target-k], index]
           
#            lookup[k] = index
#        return []

# print(Solution().twoSum([2,7,11,15], 9))

#################################  !!!!
## Subarray Sum Equals K
## https://www.jointaro.com/interviews/questions/subarray-sum-equals-k/?company=microsoft
## medium , most asked
###########

# class Solution(object):
#     def subarraySum(self, nums, k):
#         running_sum = 0
#         sum_freq = {0: 1}
#         subarray_count = 0

#         for n in nums:
#             running_sum += n

#             #Check if there is a prefix sum equal to running_sum - target_value
#             if running_sum - k in sum_freq:
#                 print(f"running_sum: {running_sum} - k: {k}, in sum_freq: {sum_freq[running_sum - k]}")
#                 subarray_count += sum_freq[running_sum - k]
            
#             sum_freq[running_sum] = sum_freq.get(running_sum, 0) + 1
#             print(sum_freq)
        
#         return subarray_count

#print(Solution().subarraySum([1], 0))
#print(Solution().subarraySum([1,2,3], 3))
# print(Solution().subarraySum([1,1,1], 2))
# print(Solution().subarraySum([1,2,1,2,1], 3))

#################################
## Group Anagrams 
## https://www.jointaro.com/interviews/questions/group-anagrams/?company=microsoft
## medium , most asked
###########

# class Solution(object):
#     def groupAnagrams(self, strs):
#         record = { }
#         for s in strs: 
#             key = "".join(sorted(s))
#             record[key] = record.get(key, []) + [s]
        
#         return list(record.values())
        
# print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

        
#########################################################3
##
# DAY Three
# Two points
# 
# left = 0
# right = len(arr) - 1

# while left < right:

#     if condition:
#         left += 1
#     else:
#         right -= 1

#################################
##  Valid Palindrome
## https://www.jointaro.com/interviews/questions/valid-palindrome/?company=microsoft
## easy , very unlikely
###########

# class Solution(object):
#     def isPalindrome(self, s):
#         s1 = "".join(c.lower() for c in s if c.isalnum())
#         print (s1)
#         left = 0
#         right = len(s1) - 1

#         while left < right:

#             if s1[left] != s1[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
    
# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# print(Solution().isPalindrome("0P"))
# print(Solution().isPalindrome(" "))

        
#################################
##  Container With Most Water
## https://www.jointaro.com/interviews/questions/container-with-most-water/?company=microsoft
## medium , unlikely
###########

# class Solution(object):
#     def maxArea(self, height):
#         left = 0
#         right = len(height) - 1
#         maxA = 0

#         while left < right:
#             area = min(height[left], height[right]) * (right - left)
#             maxA = max(maxA, area)
#             if height[left] <= height[right]:
#                 left += 1
#             else:
#                 right -= 1
    
#         return maxA
    
# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
# print(Solution().maxArea([1,1]))

#################################
##  Merge Sorted Array 
## https://www.jointaro.com/interviews/questions/merge-sorted-array/?company=microsoft
## easy , likely
###########

# class Solution(object):
#     """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#      """
#     def merge(self, nums1, m, nums2, n):
#          merged_array_length = m + n
    
#          # Initialize pointers to the end of each array.
#          first_array_pointer = m - 1
#          second_array_pointer = n - 1
#          merged_array_pointer = merged_array_length - 1

#          while first_array_pointer >= 0 and second_array_pointer >= 0:
#             if nums1[first_array_pointer] > nums2[second_array_pointer]:
#                     nums1[merged_array_pointer] = nums1[first_array_pointer] 
#                     first_array_pointer -= 1     
#             else:
#                 nums1[merged_array_pointer] = nums2[second_array_pointer]
#                 second_array_pointer -= 1
#             merged_array_pointer -= 1
            
#          # copy remaininng elements
#          while second_array_pointer >=0:
#               nums1[merged_array_pointer] = nums2[second_array_pointer]
#               second_array_pointer -= 1
#               merged_array_pointer -= 1
#          print(nums1)
               

    
# print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
# print(Solution().merge([1],1,[],0))
# print(Solution().merge([0],0,[1],1))
# print(Solution().merge([2,0],1,[1],1))

#################################
##  Two Sum II - Input Array Is Sorted
## https://www.jointaro.com/interviews/questions/two-sum-ii-input-array-is-sorted/?company=microsoft
## medium , not likely
###########
# class Solution(object):
#     def twoSum(self, numbers, target):
#         left = 0
#         right = len(numbers) - 1

#         while left <= right:
#             if numbers[left] + numbers[right] > target:
#                 right -= 1
#                 continue
#             if numbers[left] + numbers[right] < target:
#                 left += 1
#                 continue

#             return [left+1, right+1]

#         return []        
    
# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([2,3,4], 6))
# print(Solution().twoSum([-1,0], -1))
# print(Solution().twoSum([-3,3,4,90], 0))


#########################################################3
##
# DAY FOUR
# 
# Binary Search
#
#################################
##  Binary Search
## https://www.jointaro.com/interviews/questions/binary-search/?company=microsoft
## easy , unlikely
###########

# class Solution(object):
#     def search(self, nums, target):
#        left = 0
#        right = len(nums) - 1

#        while left <= right:
#            mid = (left + right) // 2

#            if nums[mid] == target:
#                return mid
           
#            if nums[mid] < target:
#                left = mid + 1 
#            else:
#                right = mid - 1

#        return -1

# print(Solution().search([-1,0,3,5,9,12], 9))
# print(Solution().search([-1,0,3,5,9,12], 2))

#################################
##  Search Insert Position
## https://www.jointaro.com/interviews/questions/search-insert-position/?company=microsoft
## easy , unlikely
###########

# class Solution(object):
#     def searchInsert(self, nums, target):
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target: 
#                 return mid
            
#             if nums[mid] < target:
#                 left = mid + 1 
#             else:
#                 right = mid - 1
        
#         return left
    
# print(Solution().searchInsert([1,3,5,6], 5))
# print(Solution().searchInsert([1,3,5,6], 2))

#################################
##  Peak Index in a Mountain Array
##  https://www.jointaro.com/interviews/questions/peak-index-in-a-mountain-array/?company=microsoft
## medium , likely
###########

# class Solution(object):
#     def peakIndexInMountainArray(self, arr):
#         left = 0
#         right = len(arr) - 1

#         while left < right:
#             mid = (left + right) // 2
#             # Check if the peak is to the left of the middle index.
#             if arr[mid - 1] > arr[mid]:
#                 right = mid
#              # Check if the peak is to the right of the middle index.
#             elif arr[mid + 1] > arr[mid]:
#                 left = mid + 1
#             else:   # Middle is peak if neither left nor right are bigger.
#                 return mid
#         return left

# class Solution(object):
#     def peakIndexInMountainArray(self, arr):
#         left = 0
#         right = len(arr) - 1

#         while left < right:
#             mid = (left + right) // 2

#             if arr[mid] < arr[mid + 1]:
#                 left = mid + 1
#             else:
#                 right = mid

#         return left
        

#print(Solution().peakIndexInMountainArray([0,1,0]))
#print(Solution().peakIndexInMountainArray([0,2,1,0]))



#########################################################3
##
# DAY FIVE
# Tree BFS / DFS
# 
# | 遍历  | 用途                    | 工具                |
# | --- | --------------------- | ----------------- |
# | DFS | 深度问题（max depth, path） | recursion / stack |
# | BFS | 层级问题（level order）     | queue             |
#
#################################
##  Maximum Depth of Binary Tree
## https://www.jointaro.com/interviews/questions/maximum-depth-of-binary-tree/?company=microsoft
## easy , unlikely
###########

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution(object):
#     def maxDepth(self, root):
#          if root == None:
#              return 0
         
#          maxLeft = self.maxDepth(root.left)
#          maxRight = self.maxDepth(root.right)

#          return max(maxLeft, maxRight) + 1

# Node = TreeNode(3, TreeNode(9,None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

# print(Solution().maxDepth(Node))
            
        
#################################
##  Binary Tree Level Order Traversal
## https://www.jointaro.com/interviews/questions/binary-tree-level-order-traversal/?company=microsoft
## medium , sometime likely
###########

# from collections import deque

# class Solution(object):
#     def levelOrder(self, root):
        
#         if not root:
#             return []

#         currentQueue = deque([root])
#         result = []
#         while currentQueue:
#             size = len(currentQueue)
#             level = []

#             for _ in range(size):
#                 node = currentQueue.popleft()
#                 level.append(node.val)

#                 if node.left:
#                     currentQueue.append(node.left)
                
#                 if node.right:
#                     currentQueue.append(node.right)

#             result.append(level)
#         return result
        
# Node = TreeNode(3, TreeNode(9,None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
# print(Solution().levelOrder(Node))
            
#################################
##  Same tree
## https://leetcode.com/problems/same-tree/
## easy , Not likely
######

# class Solution(object):
#     def isSameTree(self, p, q):
#         # 情况 1：两个都是空
#         if not p and not q:
#             return True
        
#         # 情况 2：一个空一个不空
#         if not p or not q:
#             return False
        
#         # 情况 3：值不同
#         if p.val != q.val:
#             return False
        
#         # 情况 4：递归比较左右子树
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
# p = TreeNode(1,TreeNode(2),TreeNode(3))
# q = TreeNode(1,None,TreeNode(3))

# print(Solution().isSameTree(p,q))

# class Solution(object):
#     def invertTree(self, root):
#         if not root:
#             return None
#         # swap
#         root.left, root.right = root.right, root.left

#         # recurse
#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root


# Node = TreeNode(3, TreeNode(9,None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
# print(Solution().invertTree(Node))



        


                
            