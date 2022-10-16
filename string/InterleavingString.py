"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""

class InterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2)+1)
        dp[0] = True #if all length is 0
        #suppose s1.length is 0
        for j in range(1, len(s2)+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1)+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1] #suppose s2.length is 0
            for j in range(1, len(s2)+1):
                dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1] or \
                    dp[j] and s1[i-1] == s3[i+j-1]

        return dp[-1]

