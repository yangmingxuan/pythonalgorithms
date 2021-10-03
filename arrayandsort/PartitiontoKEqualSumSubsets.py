"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""
from typing import List


class PartitiontoKEqualSumSubsets:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        quotient, remainder = divmod(total, k)
        if remainder != 0:
            return False

        def backtrace(n: int, start: int, target: int, visited: List[bool]) -> bool:
            #If a pile of items is divided into K parts evenly, and the first K-1 parts are distributed, the remaining 1 part must also be an average number
            if n == 1:
                return True
            for i in range(start, len(nums)):
                if not visited[i] and nums[i] <= target:
                    visited[i] = True
                    if nums[i] == target:
                        if backtrace(n-1, 0, quotient, visited):
                            return True
                    else:
                        if backtrace(n, i+1, target-nums[i], visited):
                            return True
                    visited[i] = False

            return False

        visited = [False] * len(nums)
        return backtrace(k, 0, quotient, visited)

