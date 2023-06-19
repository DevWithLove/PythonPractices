"""
prime number:
    1. greater than 1
    2. non-divisible by anything except one and itself

Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

You can now use math.sqrt() to calculate square roots.
sqrt(47) => 7
"""

import math

def countPrimes(n: int) -> int:		        
        if n<2:
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2,math.ceil(math.sqrt(n))):
            if isPrime[i]:
                for multiples_of_i in range(i*i,n,i):
                    isPrime[multiples_of_i] = False
        
        return sum(isPrime)


print(countPrimes(10))