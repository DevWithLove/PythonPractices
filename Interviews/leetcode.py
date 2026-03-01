# class Solution(object):
#     def twoSum(self, nums, target):
#         dict = {}
#         for index, value in enumerate(nums):
#             if value not in dict:
#                 dict[value] = index
            
#         for index, value in enumerate(nums):
#             b = target - value
#             if b in dict and index != dict[b]: 
#               return [index, dict[b]]
#         return []

###### Best Time to Buy and Sell Stock.
# class Solution(object):
#     def maxProfit(self, prices):
#          min_price = float('inf')
#          best = 0

#          for p in prices:
#              if p < min_price:
#                  min_price = p
#              else: 
#                 profit = p - min_price
#                 if profit > best:
#                      best = profit
#          return best

# print(Solution().maxProfit([7,1,5,3,6,4]))

###### Valid Word #####
# class Solution(object):
#     def isValid(self, word):
#         if len(word) < 3:
#             return False
        
#         vowels = "aeiouAEIOU"

#         w = "".join(set(word))
#         if not w.isalnum():
#             return False
        
#         numVowels = 0
#         noVowels = 0
#         for c in w:
#             if c.isdigit():
#                 continue
#             if vowels.find(c) != -1:
#                 numVowels += 1
#             else:
#                 noVowels +=1
        
#         return numVowels > 0 and noVowels > 0
        

# print(Solution().isValid("234Adas"))
# print(Solution().isValid("b3"))
# print(Solution().isValid("a3$e"))
# print(Solution().isValid("ffffff"))
# print(Solution().isValid("aaaaaaa"))

###### https://leetcode.com/problems/valid-parentheses/

# class Solution(object):
#     def isValid(self, s):
#         lookup = [ 
#             ")" : "(",
#             "}" : "{",
#             "]" : "[",
#         ]
#         open_stack = []

#         for c in s:
#             if c in lookup.values(): 
#                 open_stack.append(c)
#             elif c in lookup:
#                 if len(open_stack) == 0: 
#                     return False
                
#                 last = open_stack.pop()
#                 if lookup[c] != last:
#                     return False
        
#         return not open_stack

# class Solution(object):
#     def isValid(self, s):
#         lookup = ["()","[]","{}"]
#         stack = []
#         stack.append(s[0])
#         for i in s[1:]:
#             if len(stack) == 0:
#                 stack.append(i)
#                 continue

#             last = stack[-1]
#             if f"{last}{i}" in lookup:
#                 stack.pop()
#             else:
#                 stack.append(i)
        
#         return not stack

# print(Solution().isValid("({)})"))  

###### https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# class Solution(object):
#     def removeDuplicates(self, nums):
#         if not nums:
#             return []
        
#         unique = [nums[0]]

#         for i in range(1, len(nums)):
#             if nums[i] != unique[-1]:
#                 unique.append(nums[i])

#         return unique

        # unique = {}

        # for i in range(len(nums)):
        #     if nums[i] in unique:
        #         continue
        #     else:
        #         unique[nums[i]] = i
            
        # newNumbs = sorted(unique, key=unique.get)
        # return (len(unique), newNumbs)
        
# print(Solution().removeDuplicates([1,1,2]))      

#### https://www.jointaro.com/interviews/questions/spiral-matrix/?company=microsoft

# class Solution(object):
#     def spiralOrder(self, matrix):
#         if not matrix or not matrix[0]:
#             return []

#         res = []
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1

#         while top <= bottom and left <= right:
#             # top row
#             for c in range(left, right + 1):
#                 res.append(matrix[top][c])
#             top += 1

#             # right col
#             for r in range(top, bottom + 1):
#                 res.append(matrix[r][right])
#             right -= 1

#             # bottom row
#             if top <= bottom:
#                 for c in range(right, left - 1, -1):
#                     res.append(matrix[bottom][c])
#                 bottom -= 1

#             # left col
#             if left <= right:
#                 for r in range(bottom, top - 1, -1):
#                     res.append(matrix[r][left])
#                 left += 1

#         return res


# print(Solution().spiralOrder([[1,2,3],[4,5,6]]))     

# https://www.jointaro.com/interviews/questions/palindrome-number/?company=microsoft

#
# // 在 Python 中叫做：
# floor division（整除）
#  x = 123
# x / 10   = 12.3
# x // 10  = 12
#


# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0: 
#             return False
        
#         reverted = 0
#         numberToReveted = x
#         while numberToReveted > 0:
#             last = numberToReveted % 10
#             reverted = (reverted * 10) + last
#             numberToReveted = numberToReveted // 10
            
#         return reverted == x

# print(Solution().isPalindrome(121))

# https://www.jointaro.com/interviews/questions/roman-to-integer/?company=microsoft
# class Solution(object):
#     def romanToInt(self, s):
#         romans = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#             }

#         total = 0
#         current = len(s) - 1
#         lastValue = -1
#         while not current < 0: 
#             currentValue = romans[s[current]]

#             if lastValue == -1:
#                 total += currentValue
#             else:
#                 if currentValue >= lastValue:
#                     total += currentValue
#                 else:
#                     total -= currentValue
    
#             current -= 1
#             lastValue = currentValue

#         return total
    
# print(Solution().romanToInt("IVI"))

# class Solution(object):
#     def generateParenthesis(self, n):
#         all_valid_comb = []

#         def backtrack(current_string, open_count, close_count):
#             if len(current_string) == 2* n:
#                 all_valid_comb.append(current_string)
#                 return
            
#              # Rule: Can add an opening parenthesis if we haven't used all available.
#             if open_count < n:
#                  backtrack(current_string + '(', open_count + 1, close_count)

#             if close_count < open_count:
#                  backtrack(current_string + ')', open_count, close_count + 1)

#         backtrack("", 0, 0)
#         return all_valid_comb

# print(Solution().generateParenthesis(10))

# class Solution(object):
#     def merge(self, intervals):

#         # Sort intervals by start time.
#         intervals.sort(key=lambda interval: interval[0])

#         merged_intervals = []
    
#         for interval in intervals:
#         # If the list of merged intervals is empty or if the current
#         # interval does not overlap with the last interval, append it.
#           if not merged_intervals or merged_intervals[-1][1] < interval[0]:
#                  merged_intervals.append(interval)
#           else:
#             # Otherwise, there is overlap, so we merge the current interval
#             # with the last one.
#                   merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

#         return merged_intervals

# print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

# class Solution(object):
#     def groupAnagrams(self, strs):
#        lookup = {}

#        for s in strs:
#            s_sorted = "".join(sorted(s))
#            if s_sorted not in lookup:
#                lookup[s_sorted] = []
     
#            lookup[s_sorted].append(s)

#        return list(lookup.values())
# #        result = []
# #        for v in lookup.values():
# #             result.append(v)
# #        return result

# print(Solution().groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))

class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        end = 0  # inclusive

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # 跳出时 l,r 已经越界或不相等，真正回文是 (l+1 .. r-1)
            return l + 1, r - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)       # odd
            l2, r2 = expand(i, i + 1)   # even

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


print(Solution().longestPalindrome("babad"))  # bab or aba
#print(Solution().longestPalindrome("cbbd"))   # bb


# class Solution(object):
#     def containsDuplicate(self, nums):
#         if not len(nums) > 1:
#             return False
        
#         lookup = set(nums)
#         return len(nums) != len(lookup)
# print(Solution().containsDuplicate([1,2,3,1]))

# class Solution(object):
#    def lengthOfLongestSubstring(self,input_string):
#     longest_substring_length = 0
#     window_start_index = 0
#     characters_in_window = {}

#     for window_end_index, current_character in enumerate(input_string):
#         if current_character in characters_in_window and characters_in_window[current_character] >= window_start_index:
#             # When a repeating character is found, we need to move the window's start.
#             # This ensures the window only contains unique characters.
#             window_start_index = characters_in_window[current_character] + 1

#         # Update the last seen index of the current character.
#         characters_in_window[current_character] = window_end_index

#         # The current window size represents a valid substring without repeating characters.
#         current_window_size = window_end_index - window_start_index + 1

#         # We maintain the maximum length found so far.
#         longest_substring_length = max(longest_substring_length, current_window_size)

#     # After iterating through the entire string, we have the overall longest length.
#     return longest_substring_length


        
# print(Solution().lengthOfLongestSubstring("ohomm")) 


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         left = 0
#         longest = 0
#         char_in_string = { }

#         for right, char in enumerate(s):
           
#            if char in char_in_string and char_in_string[char] >= left: 
#                left = char_in_string[char] + 1    
        
#            char_in_string[char] = right

#            longest = max(longest, right - left + 1)

#         return longest
    
# print(Solution().lengthOfLongestSubstring("ohomm")) 
