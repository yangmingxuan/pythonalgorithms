"""
Given a string s, return the last substring of s in lexicographical order.



Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"


Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""

class LastSubstringinLexicographicalOrder:
    """
     * Explanation: 要找排序最大的子串，就是找字符串中排序最大的字符，存在相同的多个最大的字符时，比较后面的第二个字符，
     * 以此类推，直到最后
     * To find the lexicographically maximum substring is to find the highest sorted character in the string.
     * When there are multiple largest characters in the same string, compare the second character after that, and so on, until the end
    """
    def lastSubstring(self, s: str) -> str:
        slow, fast, length = 0, 1, 0
        while fast + length < len(s):
            if s[slow+length] == s[fast+length]: #if equal, compare the next character
                len += 1
            elif s[slow+length] > s[fast+length]: #the slow character is higher than fast one, compare the next first character
                fast += (length + 1)
                length = 0
            else: #the fast character is higher than slow one, compare the next sub string
                slow = fast
                fast = slow + 1
                length = 0

        return s[slow:]

