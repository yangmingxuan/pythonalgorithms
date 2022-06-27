"""
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.



Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1]
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true


Constraints:

n == target.length
1 <= n <= 5 * 10^4
1 <= target[i] <= 10^9
"""
from typing import List


class ConstructTargetArrayWithMultipleSums:
    def isPossible(self, target: List[int]) -> bool:
        total, maxnum, max_i = 0, 0, -1

        for i, num in enumerate(target):
            total += num
            if num > maxnum:
                maxnum = num
                max_i = i

        total -= maxnum
        if maxnum == 1 or total == 1:
            return True
        if maxnum <= total or total < 1 or maxnum % total == 0:
            return False
        maxnum %= total
        target[max_i] = maxnum
        return self.isPossible(target)
