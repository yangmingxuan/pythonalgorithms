"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
"""

class ReverseOnlyLetters:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s)-1
        ans = ""
        while i < len(s):
            while j >= 0 and not (s[j] >= 'A' and s[j] <= 'Z' or s[j] >= 'a' and s[j] <= 'z'):
                j -= 1
            if s[i] >= 'A' and s[i] <= 'Z' or s[i] >= 'a' and s[i] <= 'z':
                ans += s[j]
                j -= 1
            else:
                ans += s[i]
            i += 1

        return ans
