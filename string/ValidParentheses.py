"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

class ValidParentheses:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(',']':'[','}':'{'}
        match = []
        for ch in s:
            if ch not in parentheses:
                match.append(ch)
            else:
                if not match:
                    return False
                popbracket = match.pop()
                if parentheses[ch] != popbracket:
                    return False

        return not match
