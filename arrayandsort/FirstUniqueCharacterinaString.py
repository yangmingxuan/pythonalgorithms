"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.
"""
import collections


class FirstUniqueCharacterinaString:
    def firstUniqChar(self, s: str) -> int:
        if not s or len(s) == 0:
            return -1
        letters = [0] * 26
        for ch in s:
            letters[ord(ch)-ord('a')] += 1

        for i,ch in enumerate(s):
            if letters[ord(ch)-ord('a')] == 1:
                return i
        return -1

    def firstUniqChar2(self, s: str) -> int:
        if not s or len(s) == 0:
            return -1
        letters = collections.Counter(s)
        for ch in letters:
            if letters[ch] == 1:
                return s.find(ch)

        return -1;
