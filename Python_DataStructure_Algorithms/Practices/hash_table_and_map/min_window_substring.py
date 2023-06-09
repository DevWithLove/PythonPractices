"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

# def min_win_strs(s:str, t:str) -> str:
#     if len(s) < len(t):
#        return ""
#     d = dict()
#     result = s
#     for i in range(0, len(s)): 
#       if s[i] not in t: 
#          continue
#       for j in range(i, len(s)):
#         current = s[j]
#         if current in t and current not in d: 
#             d[current] = j
#             if len(d) == len(t):
#               start = min(d.values())
#               end = max(d.values())
#               lenth = end - start + 1
#               if lenth < len(result):
#                 result = s[start:end+1]
#               d.clear()
#               break
#     return result    

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)

        if(len1 < len2):
            return ""

        hashPat = {}
        hashStr = {}

        for i in range(0, len2):
            if(hashPat.get(t[i]) is None):
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(0, len1):

            if(hashStr.get(s[right]) is None):
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1
            if(hashPat.get(s[right]) is None):
                hashPat[s[right]] = 0
            if (

                hashPat.get(s[right]) != 0 and
                hashStr.get(s[right]) <= hashPat.get(s[right])
            ):
                count += 1  # keep incrementing the count if string hash is less then pattern hash
            # count==len2 means a window is found that contains all character of pattern string
            if (count == len2):

                if(hashStr.get(s[left]) is None):
                    hashStr[s[right]] = 0
                if(hashPat.get(s[left]) is None):
                    hashPat[s[right]] = 0
                while (
                    hashStr.get(s[left]) > hashPat.get(s[left]) or
                    hashPat.get(s[left]) == 0
                ):
                    #minimizing the windows range from left side

                    if (hashStr.get(s[left]) > hashPat.get(s[left])):
                        hashStr[s[left]] -= 1
                    left += 1  # incrementing the left pointer

                windowLen = right - left + 1  # calculating the windows length
                if (minLen > windowLen):
                    minLen = windowLen
                    startIndex = left

        if (startIndex == -1):
            return ""
        return s[startIndex:startIndex+minLen]

# print(min_win_strs("ADOBECODEBANC", "ABC"))
# print(min_win_strs("asawosdnodkiod", "saw"))
# print(min_win_strs("abaacad", "aca"))
# print(min_win_strs("a", "a"))
# print(min_win_strs("a", "aa"))
