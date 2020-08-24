"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry, len1, len2 = 0, len(a) - 1, len(b) - 1
        while len1 >= 0 or len2 >= 0:
            x1 = ord(a[len1]) - ord('0') if len1 >= 0 else 0
            x2 = ord(b[len2]) - ord('0') if len2 >= 0 else 0
            val = x1 + x2 + carry
            carry = val // 2
            val %= 2
            ans.append(val)
            len1 -= 1
            len2 -= 1

        if carry > 0:
            ans.append(carry)

        return ''.join(str(x) for x in ans[::-1])
