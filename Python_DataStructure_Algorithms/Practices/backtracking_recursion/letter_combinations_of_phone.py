"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

from typing import List

class Solution:

    def backtracking(self, ans, m, digits, combination, index):
        if(index > len(digits)):
            return
        if(len(combination) == len(digits)):
            ans.append(combination[:])
            return

        currentDigit = digits[index]
        curString = m[currentDigit]

        for i in range(len(curString)):
            self.backtracking(ans, m, digits, combination +
                              curString[i], index+1)

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if(len(digits) == 0):
            return ans

        m = {}

        m['2'] = "abc"
        m['3'] = "def"
        m['4'] = "ghi"
        m['5'] = "jkl"
        m['6'] = "mno"
        m['7'] = "pqrs"
        m['8'] = "tuv"
        m['9'] = "wxyz"

        self.backtracking(ans, m, digits, "", 0)

        return ans

s = Solution()
print(s.letterCombinations("23"))