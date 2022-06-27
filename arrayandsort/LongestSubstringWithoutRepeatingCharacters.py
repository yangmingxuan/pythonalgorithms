"""

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = {}
        ans, l, length = 0, 0, len(s)
        for r in range(length):
            if s[r] not in c or s[r] == 0:
                c[s[r]] = 1
            else:
                ans = max(ans, r-l)
                c[s[r]] += 1
                while c[s[r]] != 1:
                    c[s[l]] -= 1
                    l += 1

        return max(ans, length-l)
