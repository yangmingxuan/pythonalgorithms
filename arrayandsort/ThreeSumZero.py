"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class ThreeSumZero:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i, n = 0, len(nums)
        while i < n - 2:
            l, r = i+1, n-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            i += 1
            while i < n-2 and nums[i] == nums[i-1]:
                    i += 1

        return ans
