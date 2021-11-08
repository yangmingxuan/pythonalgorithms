"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"


Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""

class ReverseWordsinaString:
    def reverseWords(self, s: str) -> str:
        ans = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
                continue
            lastindex = i
            while i >= 0 and s[i] != ' ':
                i -= 1

            for j in range(i+1, lastindex+1):
                ans += s[j]
            ans += ' '
            i -= 1
        return ans[:-1]

    def reverseWords2(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))
