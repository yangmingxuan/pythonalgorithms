"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""
class MaximumNumberofBalloons:
    def maxNumberOfBalloons(self, text: str) -> int:
        bcount,acount,lcount,ocount,ncount = 0,0,0,0,0
        for ch in text:
            if ch == "b":
                bcount += 1
            elif ch == "a":
                acount += 1
            elif ch == "l":
                lcount += 1
            elif ch == "o":
                ocount += 1
            elif ch == "n":
                ncount += 1

        lcount //= 2
        ocount //= 2

        return min([bcount,acount,lcount,ocount,ncount])

    def maxNumberOfBalloons2(self, text: str) -> int:
        dct = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for ch in text:
            if ch in dct:
                dct[ch] += 1
        dct['l'] //= 2
        dct['o'] //= 2
        return min(dct.values())
