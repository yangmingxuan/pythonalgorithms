"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.



Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false


Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""

#from typing import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
        if len(word) == 1:
            return True

        if word[0].isupper() and word[1].isupper():
            #case 1 must all uppercase
            for i in range(2, len(word)):
                if not word[i].isupper():
                    return False
        else:
            #case 2, 3 from index 1 to the end must all lowwercase
            for i in range(1, len(word)):
                if not word[i].islower():
                    return False

        return True

    def detectCapitalUse2(self, word: str) -> bool:
        #all upper or all lower is True -- case 1, 2
        if word.upper() == word or word.lower() == word:
            return True

        #first is upper and else is lower is True -- case 3
        if word[0].isupper() and word[1:].lower() == word[1:]:
            return True

        return False
