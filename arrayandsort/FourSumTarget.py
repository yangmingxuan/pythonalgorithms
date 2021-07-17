"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
from typing import List


class FourSumTarget:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        i = 0
        while i < n-3:
            j = n - 1
            while j > i+2:
                l, r = i+1, j-1
                while l < r:
                    if nums[i]+nums[l]+nums[r]+nums[j] == target:
                        lsum4 = [nums[i],nums[l],nums[r],nums[j]]
                        ans.append(lsum4)
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[i]+nums[l]+nums[r]+nums[j] > target:
                        r -= 1
                    else:
                        l += 1
                while j > i+2 and nums[j-1] == nums[j]:
                    j -= 1
                j -= 1
            while i < n-3 and nums[i+1] == nums[i]:
                i += 1
            i += 1

        return ans

fst = FourSumTarget()
nums = [2,2,2,2,2]
ans = fst.fourSum(nums, 8)
