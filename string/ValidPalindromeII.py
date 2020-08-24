"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class ValidPalindromeII:
    def validPalindrome(self, s: str) -> bool:
        def isValPalindrom(s: str, i: int, j: int) -> bool:
            for k in range(i, (i + j) // 2 + 1):
                if s[k] != s[j - k + i]:
                    return False
            return True

        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                j = len(s) - i - 1
                return isValPalindrom(s, i, j - 1) or isValPalindrom(s, i + 1, j)

        return True

