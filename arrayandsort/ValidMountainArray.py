"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Strictly Increasing   Strictly Decreasing
    -------------------->------------------>
    0   2    3     4     5     2     1     0


    No Strictly Increasing  Strictly Decreasing
    --------->----->---->------------------>
    0   2    3     3     5     2     1     0


    Example 1:

    Input: arr = [2,1]
    Output: false
    Example 2:

    Input: arr = [3,5,5]
    Output: false
    Example 3:

    Input: arr = [0,3,2,1]
    Output: true


    Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^4
"""
from typing import List


class ValidMountainArray:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        while i < len(arr) - 1 and arr[i+1] > arr[i]:
            i += 1
        if i == 0 or i == len(arr) - 1:
            return False

        while i < len(arr) - 1 and arr[i+1] < arr[i]:
            i += 1

        return i == len(arr)-1
