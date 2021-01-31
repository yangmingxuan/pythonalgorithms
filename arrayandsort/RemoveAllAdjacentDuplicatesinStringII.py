"""
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"


Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
"""


class RemoveAllAdjacentDuplicatesinStringII:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        length, i = len(s), 0
        while i < length:
            if i > 0 and s[i] == s[i-1]:
                count = stack.pop() + 1
                if count == k:
                    s = s[:i-k+1] + s[i+1:]
                    length -= k
                    i -= k
                else:
                    stack.append(count)
            else:
                stack.append(1)
            i+= 1
        return s

    def removeDuplicates2(self, s: str, k: int) -> str:
        length = len(s)
        while True:
            for c in set(s):
                s = s.replace(c*k, "")
            if length == len(s):
                break
            length = len(s)
        return s