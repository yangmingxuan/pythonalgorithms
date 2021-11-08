"""
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".



Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""


Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.
"""

class LongestDuplicateSubstring:
    def longestDupSubstring(self, s: str) -> str:
        if not s:
            return s
        base = 26
        modulus = 100000000007
        self.maxlen = 0
        self.ans = ""
        nums = []
        for i in range(len(s)):
            nums.append(ord(s[i])-ord('a'))

        def existDupString(leng: int) -> int:
            h = 0
            aL = 1
            #the initial number(string)
            for i in range(leng):
                h = (h*base + nums[i]) % modulus
                aL = (aL*base) % modulus
            exist = set()
            exist.add(h)

            #move the window
            for start in range(1, len(nums)-leng+1):
                #remove the first digit and multiply by base(26)
                h = (h * base - nums[start - 1] * aL % modulus + modulus) % modulus
                #add the next digit
                h = (h + nums[start+leng-1]) % modulus

                if h in exist:
                    if self.maxlen < leng:
                        self.maxlen = leng
                        self.ans = s[start:start+leng]
                    return start

                exist.add(h)

            return -1

        low, high = 1, len(nums)
        while low <= high:
            midlen = (low+high) // 2
            if existDupString(midlen) != -1:
                #search the longer duplicate string
                low = midlen + 1
            else:
                #narrow the window
                high = midlen - 1

        return self.ans
