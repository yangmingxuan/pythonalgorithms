"""

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

n == nums.length
1 <= n <= 10^4
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class NondecreasingArray:
    def checkPossibility(self, nums: List[int]) -> bool:
        def check() -> bool:
            for i in range(len(nums)-1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        onceModify = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if not onceModify:
                    tmp = nums[i]
                    nums[i] = nums[i+1]
                    check1 = check()
                    if check1:
                        return True
                    nums[i],nums[i+1] = tmp,tmp
                    return check()
                    onceModify = True
                else:
                    return False
        return True

