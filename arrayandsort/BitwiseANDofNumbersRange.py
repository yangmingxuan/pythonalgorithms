"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0


Constraints:

0 <= left <= right <= 2^31 - 1
"""
import math


class BitwiseANDofNumbersRange:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            count += 1
        return left << count

    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        if left == 0 or right == 0: return 0
        a = math.log2(left)
        b = math.log2(right)
        #如果两个数字跨越了一个2的N次幂，那么必然有数字1后面全部是0的数字，那么按位做与运算必然为0.
        #If two numbers span a power of two's NTH power, there must be a number is 1 followed by all 0s, and then the bitwise AND must be zero.
        if int(b - a) > 0: return 0
        ans = left
        for x in range(left + 1, right + 1):
            ans = ans & x
            #if ans == 0: return 0

        return ans

ban = BitwiseANDofNumbersRange()
ans = ban.rangeBitwiseAnd2(5,7)
print(ans)
