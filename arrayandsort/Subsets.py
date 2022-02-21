"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res:List[List[int]] = []

        def dfs(idx: int, lst: List[int]):
            if idx == len(nums):
                return
            res.append([x for x in lst])
            for i in range(idx, len(nums)):
                lst.append(nums[i])
                dfs(i+1, lst)
                lst.pop()

        dfs(0, [])
        return res
"""
   def subsets2(nums: List[int]) -> List[List[int]]:
       ans = [[]]
       for num in nums:
           ans += [curr + [num] for curr in ans]
       return ans
"""