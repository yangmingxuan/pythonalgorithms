"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from typing import List


class PalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []
        n = len(s)

        def isPalindrom(i, j) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(index: int) -> None:
            if index == n:
                ans.append(tmp[:])
                return

            for i in range(index, n):
                if isPalindrom(index, i):
                    tmp.append(s[index:i+1])
                    backtrack(i+1)
                    tmp.pop()
            return

        backtrack(0)
        return ans

