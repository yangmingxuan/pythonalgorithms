"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class MajorityElement:
    def majorityElement(self, nums: List[int]) -> int:
        count, majornum = 0, nums[0]
        for num in nums:
            if count == 0:
                majornum = num

            count += 1 if majornum == num else -1

        return majornum

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
