"""
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1


Constraints:

1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
"""
from typing import List


class LongestUncommonSubsequenceII:
    def findLUSlength(self, strs: List[str]) -> int:

        #For example, t="abc" is a subsequence of s="aebdc", return true
        def containString(s: str, t: str) -> bool:
            lens, lent = len(s), len(t)
            i, j = 0, 0
            while i < lens and j < lent:
                if s[i] == t[j]:
                    j += 1
                i += 1

            return j == lent

        ans = -1
        for i in range(len(strs)):
            if len(strs[i]) < ans: continue
            isContain = False
            for j in range(len(strs)):
                if(i != j and containString(strs[j], strs[i])):
                    isContain = True
                    break
            if not isContain:
                ans = len(strs[i])

        return ans
