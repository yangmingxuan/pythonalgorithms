"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly
"""

class AddStrings:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        len1 = len(num1) - 1
        len2 = len(num2) - 1
        while len1 >= 0 or len2 >= 0:
            x1 = ord(num1[len1]) - ord('0') if len1 >= 0 else 0
            x2 = ord(num2[len2]) - ord('0') if len2 >= 0 else 0
            val = x1 + x2 + carry
            carry = val // 10
            val = val % 10
            res.append(val)
            len1 -= 1
            len2 -= 1

        if carry > 0:
            res.append(carry)

        return ''.join(str(x) for x in res[::-1])
