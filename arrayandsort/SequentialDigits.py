"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""
from typing import List


class SequentialDigits:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        tl = low
        count = 1
        while tl >= 10:
            tl //= 10
            count += 1

        req = 0
        while req < high and count < 10:
            for i in range(1, 10-count+1):
                req = 0
                for k in range(i, count+i):
                    req = req * 10 + k
                if low <= req <= high:
                    ans.append(req)
                if req > high:
                    break

            count += 1

        return ans

    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        ans = []

        #ie. 123->1234
        def findNextsequentialNumber(sqNumber: int) -> None:
            nextSqDigit = sqNumber % 10 + 1
            if nextSqDigit >= 10:
                return
            sqNumber = sqNumber * 10 + nextSqDigit #from 123->1234
            if sqNumber < low:
                findNextsequentialNumber(sqNumber)
            elif sqNumber <= high:
                ans.append(sqNumber)
                findNextsequentialNumber(sqNumber)
            else:
                return

        for i in range(1, 9):
            findNextsequentialNumber(i)

        ans.sort()
        return ans


sd = SequentialDigits()
low, high = 100, 300
ans = sd.sequentialDigits(low, high)
print(ans)
