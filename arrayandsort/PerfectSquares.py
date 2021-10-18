"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""
import math
import sys


class PerfectSquares:
    def numSquares(self, n: int) -> int:
        def isPerfectSquare(n: int) -> bool:
            x = math.sqrt(n)
            return x - math.floor(x) == 0

        #theorem on the sum of four squares or Lagrange quadratic sum theorem
        # (拉格朗日四平方数和定理)
        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        if isPerfectSquare(n):
            return 1

        i = 1
        while i*i < n:
            if isPerfectSquare(n-i*i):
                return 2
            i += 1

        return 3

    def numSquares2(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4
        if n <= 3:
            return n

        root = math.floor(math.sqrt(n))
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(1, root+1):
                perfectSquare = j*j
                if i >= perfectSquare:
                    dp[i] = min(dp[i], 1+dp[i-perfectSquare])
                else:
                    break

        return dp[n]
