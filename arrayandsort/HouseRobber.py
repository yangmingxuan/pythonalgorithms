"""

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        """
        #the DFS recursive method is easy to understand
        def robmax(start: int) -> int:
            if start >= len(nums):
                return 0
            if start == len(nums)-1:
                return nums[-1]
            if start == len(nums)-2:
                return max(nums[-2], nums[-1])

            return max(nums[start]+robmax(start+2), nums[start+1]+robmax(start+3))

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(robmax(0), robmax(1))
        """

        if not nums:
            return 0

        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]

        for i in range(2, len(dp)):
            dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])

        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre1, pre2 = nums[0], 0
        for i in range(1, len(nums)):
            tmp = pre1
            pre1 = max(nums[i]+pre2, pre1)
            pre2 = tmp

        return pre1