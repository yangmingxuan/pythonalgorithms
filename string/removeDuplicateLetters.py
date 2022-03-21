"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
"""
from collections import Counter


class removeDuplicateLetters:
    """
    * Explanation: 把还没有在栈中的字母依次压入栈中，并保证顺序小字母比大与它且后续还存在与字符串中的字母先入栈
     * Push the letters that are not yet in the stack into the stack in turn,
     * and make sure that the smaller letters are on the stack first than the letters that are larger and still exist in the subsequent string.

    """
    def removeDuplicateLetters(self, s: str) -> str:
        letterCount = Counter(s)
        stack = []

        for ch in s:
            letterCount[ch] -= 1;  #If count==0 means there is no this letter after
            if ch not in stack:
                while stack and stack[-1] > ch and letterCount[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)

        return "".join(stack)



