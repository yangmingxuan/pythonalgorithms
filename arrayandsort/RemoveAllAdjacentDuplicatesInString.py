"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.



Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"


Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
"""

class RemoveAllAdjacentDuplicatesInString:
    def removeDuplicates(self, s: str) -> str:
        ss = [x for x in s]
        slow, fast = 0, 0
        while fast < len(s):
            if slow > 0 and s[fast] == ss[slow-1]:
                slow -= 1
            else:
                ss[slow] = s[fast]
                slow += 1
            fast += 1

        return "".join(ss[:slow])

    def removeDuplicates2(self, s: str) -> str:
        ss = []
        for ch in s:
            if not ss or ch != ss[-1]:
                ss.append(ch)
            else:
                ss.pop()
        return "".join(ss)
