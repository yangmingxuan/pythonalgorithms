"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true


Constraints:

0 <= c <= 231 - 1
"""

class SumofSquareNumbers:
    def judgeSquareSum(self, c: int) -> bool:
        def isSquar(b: int) -> bool:
            if b < 2:
                return True
            l, r = 2, b//2
            while l <= r:
                mid = (l+r) // 2
                qd = mid * mid
                if qd == b:
                    return True
                if qd < b:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        a = 0
        while a*a <= c:
            if isSquar(c-a*a):
                return True
            a += 1
        return False
