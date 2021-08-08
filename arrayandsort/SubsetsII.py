"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


class SubsetsII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort();

        def backtrack(list: List[List[int]], temp: List[int], start: int):
            list.append(temp.copy())
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                backtrack(list, temp, i+1)
                temp.pop()

        lret, temp_list = [], []
        backtrack(lret, temp_list, 0)
        return lret

