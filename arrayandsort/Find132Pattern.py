"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:

n == nums.length
1 <= n <= 2 * 10^5
-10^9 <= nums[i] <= 10^9
"""
import sys
from typing import List


class Find132Pattern:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        minval = [nums[0]]
        for i in range(1, n):
            #record the minimum number from the left
            minval.append(min(nums[i], minval[-1]))

        stack = []
        for j in range(n-1, -1, -1):
            while stack and stack[-1] <= minval[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]: #now minval[j] < stack[-1] < nums[j]
                return True
            stack.append(nums[j])

        return False
