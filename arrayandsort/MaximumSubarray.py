"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        submax, allmax = nums[0], nums[0]
        for i in range(1, len(nums)):
            submax = max(submax+nums[i], nums[i])
            allmax = max(allmax, submax)

        return allmax
        """
        add = 0
        allmax = nums[0]
        for num in nums:
            add += num
            if add > allmax:
                allmax = add
            if add < 0:
                add = 0
        return allmax

