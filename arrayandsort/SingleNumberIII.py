"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]


Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
from typing import List


class SingleNumberIII:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        idx = 0
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                ans.append(nums[i])
                break
            else:
                if nums[i] != nums[i+1]:
                    ans.append(nums[i])
                    idx += 1
                    if(idx == 2):
                        break
                    else:
                        i -= 1
            i += 2

        return ans
