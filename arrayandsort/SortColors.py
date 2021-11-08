"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCur, twoCur, cur = 0, len(nums)-1, 0
        while cur <= twoCur:
            if nums[cur] == 0:
                nums[zeroCur], nums[cur] = nums[cur], nums[zeroCur]
                zeroCur += 1
                cur += 1
            elif nums[cur] == 2:
                nums[twoCur], nums[cur] = nums[cur], nums[twoCur]
                twoCur -= 1
            else:
                cur += 1

