"""

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""

class LongestValidParentheses:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        maxlen = 0
        idx = 0
        for ch in s:
            if ch == '(':
                stack.append(idx)
            else:
                stack.pop()
                if not stack: #the last pop is not (
                    stack.append(idx)
                else:
                    maxlen = max(maxlen, idx-stack[-1])
            idx += 1

        return maxlen
