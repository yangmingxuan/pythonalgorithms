"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.



Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1


Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""

class DivideTwoIntegers:
    def divide(self, dividend: int, divisor: int) -> int:
        Min = -2**31
        Max = 2**31-1
        if dividend == Min:
            if divisor == -1:  return Max
            if divisor == Min: return 1

        elif divisor == Min: return 0
        if dividend == 0: return 0

        sign = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = True

        ans = 0
        if dividend == Min:
            if sign:
                dividend += divisor
            else:
                dividend -= divisor
            ans = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend == Max:
            dividend -= divisor
            ans += 1

        while dividend >= divisor:
            tmp = divisor
            mul = 1
            while dividend >= tmp:
                dividend -= tmp
                ans += mul
                tmp += tmp
                mul += mul

        return -ans if sign else ans
