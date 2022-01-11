"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class BasicCalculatorII:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        def comparePrevious(op1: str, op2: str) -> int:
            if op1 == '+' or op1 == '-':
                if op2 == '*' or op2 == '/':
                    return -1
                else:
                    return 0
            elif op1 == '*' or op1 == '/':
                if op2 == '+' or op2 == '-':
                    return 1
                else:
                    return 0
            return 0

        def cal(num1: int, op: str, num2: int) -> int:
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                return num1 // num2

            return 0

        operator = []
        digit = []
        val = 0
        for ch in s:
            if ch == ' ':
                continue
            if ch.isdigit():
                val = val * 10 + (ord(ch) - ord('0'))
            else:
                #operator
                if not operator or comparePrevious(ch, operator[-1]) > 0:
                    # can not calculate firstly
                    digit.append(val)
                    operator.append(ch)
                    val = 0
                else:
                    #calcuate
                    while operator and comparePrevious(ch, operator[-1]) <= 0:
                        previousNum = digit.pop()
                        op = operator.pop()
                        val = cal(previousNum, op, val)
                    digit.append(val)
                    operator.append(ch)
                    val = 0

        #calculate last time
        while operator:
            previousNum = digit.pop()
            op = operator.pop()
            val = cal(previousNum, op, val)

        return val
