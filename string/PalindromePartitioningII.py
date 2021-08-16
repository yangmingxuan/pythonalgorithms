"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""

class PalindromePartitioningII:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]

        def solve(l: int, r: int):
            while l >= 0 and r < n and s[l] == s[r]:
                if l == 0:
                    #from 0 to r is Palindrome String
                    dp[r] = 0
                else:
                    #from l to r is Palindrome String, so the value is dp[l-1]+1
                    dp[r] = min(dp[l-1] + 1, dp[r])
                l -= 1
                r += 1

        for i in range(n):
            solve(i, i) #form like "a", "aba", "cabac"
            solve(i, i+1) #form like "aa", "baab", "cbaabc"

        return dp[n-1]
