"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List


class Solution:
    def findHash(self,s):
        return ''.join(sorted(s))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            if(hashed not in m):
                m[hashed] = []
            m[hashed].append(s)
        
        for p in m.values():
            answers.append(p)
        
        return answers


def group_anagrams(strs: List[str]) -> List[List[str]]:
   dict = {int:List}
   for n in strs:
      code = 0 
      for c in n:
         code += ord(c)
      if code in dict: 
         dict[code].append(n)
      else:
         dict[code] = [n]
   return [value for (key, value) in dict.items()]

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))