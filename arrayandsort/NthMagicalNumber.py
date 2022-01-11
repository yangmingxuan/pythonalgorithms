"""
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
Example 3:

Input: n = 5, a = 2, b = 4
Output: 10
Example 4:

Input: n = 3, a = 6, b = 4
Output: 8


Constraints:

1 <= n <= 10^9
2 <= a, b <= 4 * 10^4
"""

class NthMagicalNumber:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        #Greatest common divisor 最大公约数
        def GCD(x: int, y: int) -> int:
            if x== 0:
                return y
            return GCD(y%x, x)

        MOD = 1000000007
        gcd = GCD(a, b)
        lcm = a*b // gcd  #Least common multiple 最小公倍数
        lo, hi = 0, n*min(a,b)
        while lo < hi:
            mid = (lo+hi)//2
            #If there are not enough magic numbers below mid
            if mid//a + mid//b - mid//lcm < n:
                lo = mid + 1
            else:
                hi = mid

        return lo%MOD

