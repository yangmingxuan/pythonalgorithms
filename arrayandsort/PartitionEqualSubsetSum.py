"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class PartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        def backtrack(idx: int, left: int, dp: List[bool]) -> bool:
            if left == 0:
                return True
            if idx >= len(nums) or left < 0:
                return False

            if dp[left] is not None:
                return dp[left]

            dp[left] = backtrack(idx+1, left-nums[idx], dp) or backtrack(idx+1, left, dp)
            return dp[left]

        sumall = sum(nums)
        if sumall % 2 != 0:
            return False

        sumall //= 2

        dp = [None] * (sumall+1)

        return backtrack(0, sumall, dp)
