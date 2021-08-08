"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
import sys
from typing import List


class ThreeSumClosest:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff, length = sys.maxsize, len(nums)
        nums = sorted(nums)

        for i in range(length-2):
            left, right = i+1, length - 1
            while left < right:
                ans = nums[i] + nums[left] + nums[right]
                if abs(ans-target) < abs(diff):
                    diff = ans - target
                if diff == 0:
                    break
                elif ans - target < 0:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                break

        return target+diff

abc = [-1,2,1,-4,4,5,8]
tsc = ThreeSumClosest()
ans = tsc.threeSumClosest(abc, 1)
