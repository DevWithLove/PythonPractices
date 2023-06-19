"""
abcabcbd => 3
aaaaaa=> 1
'' => 0
abcbda => 4, cbda
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while(left<n and right<n):
            el = s[right]
            if(el in m):
                left = max(left,m[el]+1)
            m[el] = right
            ans = max(ans,right-left+1)
            right+=1
        return ans


def longest_substring(input) -> int:
    if len(input) <= 1:
        return len(input)
    seen = set()
    max_length = 0
    i = 0
    j = 0
    while j < len(input):
       currentChar = input[j] 
       if currentChar in seen:
           seen.remove(input[i])
           i += 1
           continue               
       else:
           seen.add(currentChar)
           max_length = max(max_length, j - i + 1)
       j += 1
    return max_length
        



# def longest_substring(input: str) -> int:
#     if len(input) <= 1:
#         return len(input)
#     max_length = 0
#     for i in range(len(input)):
#         seen = set()
#         current_length = 0
#         for j in range(i, len(input)):
#             currentChar = input[j]
#             if currentChar in seen:
#                 break
#             current_length += 1
#             seen.add(currentChar)
#             max_length = max(max_length, current_length)
#     return max_length

print(longest_substring(""))
print(longest_substring("aaaa"))
print(longest_substring("abcabcbd"))
print(longest_substring("abcbda"))
print(longest_substring("accde"))
print(longest_substring("acdceca"))
        