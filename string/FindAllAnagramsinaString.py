"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from typing import List


class FindAllAnagramsinaString:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if not s or len(s) == 0:
            return ans

        originchar = [0] * 26
        for ch in p:
            originchar[ord(ch)-ord('a')] += 1

        comparachar = [0] * 26
        m, n = len(s), len(p)
        for i in range(m):
            comparachar[ord(s[i])-ord('a')] += 1
            if i >= n:
                comparachar[ord(s[i-n])-ord('a')] -= 1

            if originchar == comparachar:
                ans.append(i-n+1)

        return ans

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        ans = []
        if not s or len(s) == 0 or len(s) < len(p):
            return ans

        originhash = 0
        for ch in p:
            originhash += hash(ch)

        comparahash, m, n = 0, len(s), len(p)
        for i in range(m):
            comparahash += hash(s[i])
            if i >= n:
                comparahash -= hash(s[i-n])

            if originhash == comparahash:
                ans.append(i-n+1)

        return ans
