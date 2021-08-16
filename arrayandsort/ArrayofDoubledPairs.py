"""
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.



Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false


Constraints:

2 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105
"""
import collections
from typing import List


class ArrayofDoubledPairs:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        arr.sort(key = abs)
        for num in arr:
            #already paired
            if count[num] == 0:
                continue
            if count[num*2] <= 0:
                return False
            count[num] -= 1
            count[num*2] -= 1

        return True

    def canReorderDoubled2(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)

        for num in sorted(count, key=abs):
            if count[num] == 0:
                continue
            if count[num * 2] < count[num]:
                return False

            count[num * 2] -= count[num]

        return True
