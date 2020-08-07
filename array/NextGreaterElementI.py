from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict = {}
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num :
                dict[stack.pop()] = num

            stack.append(num)

        while len(stack) > 0 :
            dict[stack.pop()] = -1

        """
        result = []
        for num in nums1:
            result.append(dict.get(num))

        return result
        """
        return [dict.get(num, -1) for num in nums1]