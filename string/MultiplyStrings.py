"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class MultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" == num1 or "0" == num2:
            return "0"

        sumall = [0] * (len(num1)+len(num2)-1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                sumall[i+j] += int(num1[i]) * int(num2[j])

        for i in range(len(sumall)-1, 0, -1):
            sumall[i-1] += sumall[i] // 10
            sumall[i] %= 10

        return "".join([str(i) for i in sumall])
        #return str(int(num1) * int(num2))
