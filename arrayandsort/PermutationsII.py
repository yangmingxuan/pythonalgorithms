"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List


class PermutationsII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def helper(idx: int) -> None:
            if idx == n - 1:
                ans.append([x for x in nums])
                return
            seen = set()
            for i in range(idx, n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    if nums[i] != nums[idx]:
                        nums[i], nums[idx] = nums[idx], nums[i]
                    helper(idx+1)
                    if nums[i] != nums[idx]:
                        nums[i], nums[idx] = nums[idx], nums[i] #recover
            return

        helper(0)
        return ans
