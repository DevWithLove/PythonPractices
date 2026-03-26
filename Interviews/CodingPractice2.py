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
    
# print(Solution().lengthOfLongestSubstring("bbbbb"))
# print(Solution().lengthOfLongestSubstring("abcabcbb"))
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


# print(Solution().subarraySum([1], 0))
# print(Solution().subarraySum([1,2,3], 3))
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

############################
##  DAY 6  
######

###
### https://www.jointaro.com/interviews/questions/balanced-binary-tree/?company=microsoft
### easy, very unlikely

# class Solution(object):
#     def isBalanced(self, root):
#         def height(node):
#             if not node:
#                 return 0
            
#             leftHeight = height(node.left)
#             if leftHeight == -1:
#                 return -1
            
#             rightHeight = height(node.right)
#             if rightHeight == -1:
#                 return -1
            
#             if abs(leftHeight - rightHeight) > 1:
#                 return -1

#             return max(leftHeight, rightHeight) + 1

#         return height(root) != -1

# Lowest Common Ancestor of a Binary Tree
##https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
## medium , not likely

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
        
#         if not root:
#             return None
        
#         if root == p or root == q:
#             return root
    
#         leftNode = self.lowestCommonAncestor(root.left, p,q)
        
#         rightNode = self.lowestCommonAncestor(root.right, p,q)
        
#         if leftNode and rightNode:
#             return root
        
#         return leftNode if leftNode else rightNode


############################
##  DAY 7
## 把 Graph = Tree + visited 思维建立起来
######

### Number of Islands
## https://www.jointaro.com/interviews/questions/number-of-islands/?company=microsoft
### medium not likely

# class Solution(object):
#     def numIslands(self, grid):
#         if not grid or not grid[0]:
#             return 0
    
#         rows = len(grid)
#         columns = len(grid[0])
#         islands_count = 0

#         def strinkIsland(r, c):
#             #no need to chck
#             if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
#                 return
            
#             grid[r][c] = "0"
#             # Recursively explore adjacent land cells (up, down, left, right).
#             strinkIsland(r+1, c)
#             strinkIsland(r-1, c)
#             strinkIsland(r, c + 1)
#             strinkIsland(r, c - 1)
        
#          # Iterate through each cell of the grid.
#         for r in range(rows):
#             for c in range(columns):
#                  # If we find a land cell ('1'), it signifies the start of a new island.
#                 if grid[r][c] == "1":
#                     islands_count += 1
#                     # Sink all connected land parts of this newly found island.
#                     strinkIsland(r, c)
        
#         return islands_count


      
# print(Solution().numIslands([
#   ["1","1","0","1","0"],
# #   ["1","1","0","1","0"],
# #   ["1","1","0","0","0"],
# #   ["0","0","0","0","0"]
# ]))
        
#### minEdgeReversals
### https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
### hard, very likely

#from collections import defaultdict

# class Solution(object):
#     def minEdgeReversals(self, n, edges):
#         #graph = defaultdict(list)
#         graph = [[] for _ in range(n)]
#         # Build graph with direction cost
#         for u, v in edges:
#             graph[u].append((v, 0))  # original direction u -> v
#             graph[v].append((u, 1))  # reverse direction would cost 1

#         ans = [0] * n

#         # ------------------------
#         # First DFS: compute ans[0]
#         # ------------------------
#         def dfs1(node, parent):
#             total = 0
#             for nei, cost in graph[node]:
#                 if nei == parent:
#                     continue
#                 total += cost + dfs1(nei, node)
#             return total

#         ans[0] = dfs1(0, -1)

#         # ------------------------
#         # Second DFS: reroot DP
#         # ------------------------
#         def dfs2(node, parent):
#             for nei, cost in graph[node]:
#                 if nei == parent:
#                     continue

#                 # If original direction is node -> nei (cost == 0)
#                 # rerooting to nei adds 1 reversal
#                 # If original direction is nei -> node (cost == 1)
#                 # rerooting to nei subtracts 1 reversal
#                 ans[nei] = ans[node] + (1 if cost == 0 else -1)

#                 dfs2(nei, node)

#         dfs2(0, -1)
#         return ans
    
# print(Solution().minEdgeReversals(3, [[1,2],[2,0]]))
# print(Solution().minEdgeReversals(4, [[2,0],[2,1],[1,3]]))

# class Solution(object):
#     def spiralOrder(self, matrix):
#         if not matrix:
#             return []
        
#         result = []
#         top = 0
#         bottom = len(matrix) - 1
#         left = 0
#         right = len(matrix[0]) - 1
        
#         while top <= bottom and left <= right:
            
#             # 1. left → right
#             for col in range(left, right + 1):
#                 result.append(matrix[top][col])
#             top += 1
            
#             # 2. top → bottom
#             for row in range(top, bottom + 1):
#                 result.append(matrix[row][right])
#             right -= 1
            
#             # 3. right → left
#             if top <= bottom:
#                 for col in range(right, left - 1, -1):
#                     result.append(matrix[bottom][col])
#                 bottom -= 1
            
#             # 4. bottom → top
#             if left <= right:
#                 for row in range(bottom, top - 1, -1):
#                     result.append(matrix[row][left])
#                 left += 1
        
#         return result
    
# print(Solution().spiralOrder([[1,2,3]]))
# class Solution(object):
#     def countPalindromes(self, s):
#         MOD = 10**9 + 7
#         nums = [int(c) for c in s] 
#         n = len(nums)

#         # ---------- build right side counts ----------
#         R1 = [0]*10
#         R2 = [[0]*10 for _ in range(10)]  # pairs (a,b) in suffix

#         for x in reversed(nums):
#             # x becomes the first of a pair (x,b) with any b already seen on right
#             for b in range(10):
#                 R2[x][b] = (R2[x][b] + R1[b]) % MOD
#             R1[x] += 1

#         # ---------- scan centers ----------
#         L1 = [0]*10
#         L2 = [[0]*10 for _ in range(10)]  # pairs (a,b) in prefix

#         ans = 0
#         for x in nums:
#             # remove current x from RIGHT (so right means positions after center)
#             R1[x] -= 1
#             # removing x affects pairs starting with x: (x,b) decrease by R1[b]
#             for b in range(10):
#                 R2[x][b] = (R2[x][b] - R1[b]) % MOD

#             # count palindromes with this center
#             for a in range(10):
#                 for b in range(10):
#                     ans = (ans + L2[a][b] * R2[b][a]) % MOD

#             # add current x to LEFT (so left means positions before next center)
#             for a in range(10):
#                 L2[a][x] = (L2[a][x] + L1[a]) % MOD
#             L1[x] += 1

#         return ans % MOD

# print(Solution().countPalindromes("103301"))
        
# class Solution(object):
#     def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):

#         def can_make(machine_idx, x):
#             total = 0
#             for j in range(n):
#                 need = x * composition[machine_idx][j]
#                 buy = max(0, need - stock[j])
#                 total += buy * cost[j]
#                 if total > budget:
#                     return False
#             return total <= budget  
        
#         def max_for_machine(machine_idx):
#             left, right = 0, 10**9
#             while left <= right:
#                 mid = (left + right) // 2
#                 if can_make(machine_idx, mid):
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return right

#         ans = 0
#         for i in range(k):
#             ans = max(ans, max_for_machine(i))
#         return ans

# print(Solution().maxNumberOfAlloys(3,2,15,[[1,1,1],[1,1,10]],[0,0,0],[1,2,3]))

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):

#         # 确保 nums1 是较短数组
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1

#         m, n = len(nums1), len(nums2)
#         total = m + n
#         half = (total + 1) // 2

#         left, right = 0, m

#         while left <= right:
#             i = (left + right) // 2
#             j = half - i

#             nums1_left = float('-inf') if i == 0 else nums1[i-1]
#             nums1_right = float('inf') if i == m else nums1[i]

#             nums2_left = float('-inf') if j == 0 else nums2[j-1]
#             nums2_right = float('inf') if j == n else nums2[j]

#             if nums1_left <= nums2_right and nums2_left <= nums1_right:

#                 if total % 2:
#                     return max(nums1_left, nums2_left)

#                 return (max(nums1_left, nums2_left) +
#                         min(nums1_right, nums2_right)) / 2

#             elif nums1_left > nums2_right:
#                 right = i - 1
#             else:
#                 left = i + 1

# print(Solution().findMedianSortedArrays([1,2],[3,4]))

# class Solution(object):
#     def minDifficulty(self, jobDifficulty, d):

#         n = len(jobDifficulty)

#         if d > n: 
#             return - 1

#         if d == n:
#             return sum(jobDifficulty)
        
#         dp = [[float('inf')] * (d+1) for _ in range(n+1)]
#         dp[0][0] = 0

#         for i in range(1, n+1):
#             for k in range(1, d+1):
                
#                 max_job = 0
                
#                 for j in range(i, 0, -1):
                    
#                     max_job = max(max_job, jobDifficulty[j-1])
                    
#                     dp[i][k] = min(
#                         dp[i][k],
#                         dp[j-1][k-1] + max_job
#                     )
        
#         return dp[n][d]

# print(Solution().minDifficulty([6,5,4,3,2,1], 2))
        
# class Solution(object):
#     def longestPalindrome(self, s):
#         if not s: 
#             return ""

#         def expand(l, r):
#             while l >=0 and r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#              # when loop ends, (l, r) is one step beyond palindrome
#             return l+1, r - 1
        
#         best_l = 0
#         best_r = 0

#         for i in range(len(s)):
#             # odd length
#             l1, r1 = expand(i, i)
#             if r1 - l1 > best_r - best_l:
#                 best_l, best_r = l1, r1
            
#             # eveen
#              # even length
#             l2, r2 = expand(i, i + 1)
#             if r2 - l2 > best_r - best_l:
#                 best_l, best_r = l2, r2
    
#         return s[best_l:best_r + 1]
    

# class Solution(object):
#     def trap(self, height):
#         if not height:
#             return 0

#         l, r = 0, len(height) - 1
#         leftMax, rightMax = 0, 0
#         water = 0

#         while l < r:
#             if height[l] < height[r]:
#                 if height[l] >= leftMax:
#                     leftMax = height[l]
#                 else:
#                     water += leftMax - height[l]
#                 l += 1
#             else:
#                 if height[r] >= rightMax:
#                     rightMax = height[r]
#                 else:
#                     water += rightMax - height[r]
#                 r -= 1

#         return water

# print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))


##LRU Cache
### https://www.jointaro.com/interviews/questions/lru-cache/?company=microsoft
####
# class Node(object):
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache(object):
 

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {}
#         self.head = Node(0,0)
#         self.tail = Node(0,0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def remove(self, node):
#         prev_node = node.prev
#         next_node = node.next
#         node.prev.next = next_node
#         node.next.prev = prev_node
    
#     def insert(self, node):
#         prev_last = self.tail.prev
#         prev_last.next = node
#         node.prev = prev_last
#         node.next = self.tail
#         self.tail.prev = node
        

#     def get(self, key):
#         if key not in self.cache:
#             return -1
        
#         node = self.cache[key]
#         self.remove(node)
#         self.insert(node)
#         return node.val

#     def put(self, key, value):
#         if key in self.cache:
#             node = self.cache[key]
#             self.remove(node)
#         node = Node(key, value)
#         self.insert(node)
#         self.cache[key] = node
       
#         if len(self.cache) > self.capacity:
#                 headNode = self.head.next
#                 self.remove(headNode)
#                 del self.cache[headNode.key]

# class Solution(object):
#     def subsetsWithDup(self, nums):
#         nums.sort()
#         result = []
#         path = []

#         def dfs(start):
#             result.append(path[:]) #复制一份 list
#             for i in range(start, len(nums)):
#                 if i > start and nums[i]==nums[i-1]:
#                     continue
#                 path.append(nums[i])
#                 dfs(i+1)
#                 path.pop()
#         dfs(0)
#         return result

# class Solution(object):
#     def subsetsWithDup(self, nums):
#         nums.sort()
#         result = []
#         path = []

#         def dfs(start):
#             print("record:", path)
#             result.append(path[:])

#             for i in range(start, len(nums)):
#                 if i > start and nums[i] == nums[i - 1]:
#                     print("skip:", nums[i], "at index", i)
#                     continue

#                 path.append(nums[i])
#                 print("append ->", path)
#                 dfs(i + 1)
#                 path.pop()
#                 print("pop ->", path)

#         dfs(0)
#         return result
        
# print(Solution().subsetsWithDup([1,2,2]))

# class Solution(object):
#     def isHappy(self, n):
#       def next_num(n):
#         total = 0
#         while n > 0:
#             j = n % 10 
#             total += j * j
#             n = n // 10
#         return total

#       seen = set()

#       while n != 1 and n not in seen:
#         seen.add(n)
#         n = next_num(n)
      
#       return n == 1
    
# print(Solution().isHappy(2))

# class ListNode(object):

#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next 

# class Solution(object):
#     def reverseKGroup(self, head, k):
#         dummy = ListNode(0)
#         dummy.next = head
#         groupPrev = dummy

#         while True:
#             # 找到这一组的第 k 个节点
#             kth = groupPrev
#             for _ in range(k):
#                 kth = kth.next
#                 if not kth:
#                     return dummy.next

#             groupNext = kth.next

#             # 翻转这一组
#             prev = groupNext
#             curr = groupPrev.next

#             while curr != groupNext:
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp

#             # 重新连接
#             temp = groupPrev.next   # 翻转前的组头，翻转后会变成组尾
#             groupPrev.next = kth    # 接到新的组头
#             groupPrev = temp        # 移动到新的组尾

# head = ListNode(1, next = ListNode(2, next = ListNode(3, next= ListNode(4, ListNode(5)))))
# print(Solution().reverseKGroup(head, 2))


# class Solution(object):
#     def isHappy(self, n):
        

#         def next_num(n):
#             total = 0
#             while n > 0:
#                 d = n % 10
#                 total += d * d
#                 n //= 10
#             return total

#         seen = set()

#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = next_num(n)

#         return n == 1
    
# class Solution(object):
#     def isPalindrome(self, x):

#         if x < 0:
#             return False

#         if x % 10 == 0 and x != 0:
#             return False

#         reversed_half = 0

#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10

#         return x == reversed_half or x == reversed_half // 10
# print(Solution().isPalindrome(121))

# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         result = {}

#         for i in range(len(nums) - 2):
#             # 第一个数去重
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             left = i + 1
#             right = len(nums) - 1

#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]

#                 if total < 0:
#                     left += 1
#                 elif total > 0:
#                     right -= 1
#                 else:
#                     v = [nums[i], nums[left], nums[right]].sort()
#                     key = "".join([nums[i], nums[left], nums[right]]) 
#                     if key not in result:
#                         result[key] = v
#                     left += 1
#                     right -= 1

#         return result


#######################
## *** Construct Binary Tree from Preorder and Inorder Traversal  (Real)
## https://www.jointaro.com/interviews/questions/construct-binary-tree-from-preorder-and-inorder-traversal/?company=microsoft
##
# preorder（前序遍历）：根 -> 左 -> 右
# inorder（中序遍历）：左 -> 根 -> 右
#######################

# class Solution(object):

#     def buildTree(self, preorder, inorder):

#         if not preorder or not inorder:
#             return None
        
#         root_val = preorder[0]
#         root = TreeNode(root_val)

#         mid = inorder.index(root_val)
        
#         left_inorder = inorder[:mid]
#         right_inorder = inorder[mid+1:]

#         left_size = len(left_inorder)

#         left_preorder = preorder[1:1+left_size]
#         right_preorder = preorder[1+left_size:]

#         root.left = self.buildTree(left_preorder, left_inorder)
#         root.right = self.buildTree(right_preorder, right_inorder)

#         return root
    
# print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))


# class Solution(object):
#     def subsetsWithDup(self, nums):
#         nums.sort()

#         result = []
#         subset = []

#         def backtrack(index):
#             result.append(subset[:])
#             for i in range(index, len(nums)):
#                 subset.append(nums[i])
#                 backtrack(i+ 1)
#                 subset.pop()

#         backtrack(0)

#         return result

# print(Solution().subsetsWithDup([1,2]))        
        



# def merge_sort(nums):

#     if len(nums) <= 1:
#         return nums

#     mid = len(nums)//2

#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])

#     return merge(left, right)


# def merge(left, right):

#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):

#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# merge_sort([2,1,5,3])

    
# class Solution(object):
#     def numIslands(self, grid):
#         if not grid:
#             return 0
#         rows = len(grid)
#         cols = len(grid[0])
#         def dfs(row, col):
#             if row < 0 or col < 0 or row >= rows or col >= cols:
#                 return 
            
#             if grid[row][col] == "0":
#                 return 
            
#             grid[row][col] = "0"

#             dfs(row, col +1)
#             dfs(row, col -1)
#             dfs(row+1, col)
#             dfs(row-1, col)

#         count = 0
#         for r in grid:
#             for c in grid[r]:
#                 if grid[r,c] == "1":
#                     count+=1
#                     dfs(r,c)
#         return count

#https://www.jointaro.com/interviews/questions/course-schedule/?company=microsoft
# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         graph = { }

#         for i in range(numCourses):
#             graph[i] = []

#         indegree = [0] * numCourses

#         for pair in prerequisites:
#             course = pair[0]
#             pre = pair[1]

#             graph[pre].append(course)
#             indegree[course] += 1

#         queue = []

#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)
            
#         index = 0
#         taken = 0
        
#         while index < len(queue):
#             current = queue[index]
#             index += 1
#             taken += 1

#             for neighbour in graph[current]:
#                 indegree[neighbour] -= 1

#                 if indegree[neighbour] == 0:
#                     queue.append(neighbour)
#         return taken == numCourses

# print(Solution().canFinish(2, [[1,0]]))
# class Solution(object):
#     def subsets(self, nums):
#         nums.sort()
#         result = []
#         def dfs(start, path):
#             result.append(path[:])

#             for i in range(start, len(nums)):
#                 if i > start and nums[i] == nums[i-1]: 
#                     continue

#                 path.append(nums[i])
#                 dfs(i+1,path)
#                 path.pop()

#         dfs(0,[])
#         return result

# print(Solution().subsets([1,2,3]))

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         left = 0
#         count = 0
#         lookup = { }
#         for right, ch in enumerate(s):
#             if ch in lookup and lookup[ch] >= left:
#                 left = lookup[ch] + 1
            
#             lookup[ch] = right
#             count = max(count, right-left +1)
        
#         return count


# class Solution(object):
#     def topKFrequent(self, nums, k):
#         lookup = {}

#         for n in nums:
#             lookup[n] = lookup.get(n, 0) + 1

#         buckets = []
#         for i in range(len(nums) + 1):
#             buckets.append([])
    
#         for n in lookup:
#             freq = lookup[n]
#             buckets[freq].append(n)
        
#         result = []
       
#         for freq in range(len(buckets) - 1, 0, -1):
#             for num in buckets[freq]:
#                 result.append(num)
#                 if len(result) == k:
#                     return result

############

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def modifiedList(self, nums, head):
         
#          s = set(nums)
#          dummy = ListNode()
#          dummy.next = head

#          prev = dummy
#          node = head

#          while node: 
#              if node.val in s:
#                  prev.next = node.next
#              else:
#                  prev = node

#              node = node.next
             
#          return dummy.next
             
# head = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# print(Solution().modifiedList([1,2,3], head))


# class Solution(object):
#     def letterCombinations(self, digits):
         
#          if not digits:
#              return []

#          lookup = {
#              "2" : ["a", "b","c"],
#              "3" : ["d", "e", "f"],
#              "4" : ["g", "h", "i"],
#              "5" : ["j", "k", "l"],
#              "6" : ["m","n","o"],
#              "7" : ["p", "q","r","s"],
#              "8" : ["t", "u", "v"],
#              "9" : ["w", "x", "y", "z"]
#           }
         
#          result = []

#          def dfs(index, path):
#              if index == len(digits):
#                 result.append(path)
#                 return
#              letters = lookup[digits[index]]
#              for ch in letters:
#                 dfs(index+1, path + ch)
            
#          dfs(0, "")
#          return result

# print(Solution().letterCombinations("23"))


        
