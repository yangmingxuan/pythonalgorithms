"""
CombinationSumIV
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
"""
from typing import List


class CombinationSumIV:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                num_before = i - num
                if num_before >= 0:
                    dp[i] += dp[num_before]
        return dp[target]
        """
        memo = {}

        def bt(rem):
            if rem == 0:
                return 1
            if rem in memo:
                return memo[rem]
            count = 0
            for num in nums:
                if num <= rem:
                    this_count = bt(rem - num)
                    count += this_count
            memo[rem] = count
            return count

        return bt(target)

