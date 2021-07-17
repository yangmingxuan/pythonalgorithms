"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List


class ValidTriangleNumber:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        #After sorting, just verify that the sum of the two short sides is greater than
        #the third side to form a valid triangle
        nums = sorted(nums)

        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1

        return count

    def triangleNumber2(self, nums: List[int]) -> int:
        count = 0
        nums = sorted(nums)
        for k in range(len(nums)-1, 1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j-i #indicates that the sum of nums[i] to nums[j-1] plus nums[j] will be greater than nums[k]
                    j -= 1
                else:
                    i += 1

        return count


nums = [24,3,82,22,35,84,19]
vtn = ValidTriangleNumber()
ans = vtn.triangleNumber2(nums)
