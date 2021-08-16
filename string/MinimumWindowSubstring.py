"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class MinimumWindowSubstring:
    """
    Use two pointers to create a window of letters in S, which would have all the characters from T.
    Since you have to find the minimum window in S which has all the characters from T, you need to expand and contract the window using the two pointers and keep checking the window for all the characters. This approach is also called Sliding Window Approach.

    L ------------------------ R , Suppose this is the window that contains all characters of T

        L----------------- R , this is the contracted window. We found a smaller window that still contains all the characters in T

    When the window is no longer valid, start expanding again using the right pointer.
    """
    def minWindow(self, s: str, t: str) -> str:
        tm = [0] * 128
        left, right, lb, rb = 0, 0, 0, 0
        minLen = len(s) + 1
        total = len(t)  #record if all found

        #initial
        for ch in t:
            tm[ord(ch)] += 1

        while right < len(s):
            if tm[ord(s[right])] > 0:
                total -= 1
            tm[ord(s[right])] -= 1
            #if window all include
            while total == 0:
                if minLen > right + 1 - left:
                    minLen = right + 1 - left
                    lb, rb = left, right + 1
                tm[ord(s[left])] += 1
                if tm[ord(s[left])] > 0:
                    total += 1
                left += 1 #narrow the window
            right += 1


        return "" if rb == lb else s[lb:rb]
