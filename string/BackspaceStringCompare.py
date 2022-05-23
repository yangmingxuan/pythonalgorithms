"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
"""

class BackspaceStringCompare:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptrS, ptrT = len(s)-1, len(t)-1
        backS, backT = 0, 0
        while(ptrS >= 0 or ptrT >= 0):
            while ptrS >= 0:
                if s[ptrS] == '#':
                    backS += 1
                    ptrS -= 1
                elif backS > 0:
                    backS -= 1
                    ptrS -= 1
                else:
                    break

            while ptrT >= 0:
                if t[ptrT] == '#':
                    backT += 1
                    ptrT -= 1
                elif backT > 0:
                    backT -= 1
                    ptrT -= 1
                else:
                    break

            if (ptrS >= 0) != (ptrT >= 0):
                return False
            if ptrS >= 0 and ptrT >= 0 and s[ptrS] != t[ptrT]:
                return False
            ptrS -= 1
            ptrT -= 1

        return True
