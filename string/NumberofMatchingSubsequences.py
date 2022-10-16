"""
NumberofMatchingSubsequences
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(s: str, w: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(w):
                if s[i] == w[j]:
                    j += 1
                i += 1

            return j == len(w)

        allwords = {}
        for word in words:
            if word not in allwords:
                allwords[word] = 1
            else:
                allwords[word] += 1

        ans = 0
        for word in allwords.keys():
            if isSubseq(s, word):
                ans += allwords[word]

        return ans
