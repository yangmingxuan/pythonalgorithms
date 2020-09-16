"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""
from typing import List

class LargerNumKey(int):
    def __lt__(a, b):
        longa,longb,x,y = a*10, b*10, a//10, b//10
        while x > 0:
            longb *= 10
            x //= 10
        while y > 0:
            longa *= 10
            y //= 10
        return longa+b > longb+a

class LargerStrKey(str):
    def __lt__(a, b):
        return a+b > b+a

class LargestNumber:
    def largestNumber(self, nums: List[int]) -> str:
        #largenumber = ''.join(map(str,sorted(nums, key=LargerNumKey)))
        largenumber = ''.join(sorted(map(str, nums), key=LargerStrKey))
        return "0" if largenumber[0] == '0' else largenumber
