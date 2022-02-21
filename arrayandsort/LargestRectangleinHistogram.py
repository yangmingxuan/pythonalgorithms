"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""
from typing import List


class LargestRectangleinHistogram:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_i = [0] * n   #index of the first bar the left that is lower than current
        right_i = [0] * n  #index of the first bar the right that is lower than current
        left_i[0] = -1
        right_i[-1] = n

        for i in range(1, n):
            tmp = i -1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            left_i[i] = tmp

        for i in range(n-2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp

        ans = 0
        for i in range(n):
            ans = max(ans, (right_i[i]-left_i[i]-1) * heights[i])

        return ans

    def largestRectangleArea2(self, heights: List[int]) -> int:
        ans, idx = 0, 0
        n = len(heights)
        stack = [0] * (n+2)
        stack[0] = -1
        for i in range(n+1):
            while idx > 0 and heights[stack[idx]] > (heights[i] if i != n else 0):
                h = heights[stack[idx]]
                idx -= 1
                ans = max(ans, h * (i-stack[idx]-1))

            idx += 1
            stack[idx] = i

        return ans
