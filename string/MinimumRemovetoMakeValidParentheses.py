"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

class MinimumRemovetoMakeValidParentheses:
    def minRemoveToMakeValid(self, s: str) -> str:
        if s == None or len(s) == 0:
            return s

        delete = set()
        stack = []

        #get extra )
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    delete.add(i)

        # get extra (
        delete.union(set(stack))

        stringBuilder = []
        for i, c in enumerate(s):
            if i not in delete:
                stringBuilder.append(c)


        return "".join(stringBuilder)

    def minRemoveToMakeValid2(self, s: str) -> str:
        if s == None or len(s) == 0:
            return s

        # step 1: remove extra )
        firststep = []
        left = 0
        match = 0
        for i, c in enumerate(s):
            if c == '(':
                left += 1
                match += 1
            elif c == ')':
                if match == 0:
                    continue
                else:
                    match -= 1
            firststep.append(c)


        # setp 2: remove extra (
        ans = []
        keep = left - match
        for c in firststep:
            if c == '(':
                keep -= 1
                if keep < 0:
                    continue

            ans.append(c)

        return "".join(ans)
