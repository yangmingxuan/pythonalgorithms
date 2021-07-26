"""
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.



Example 1:

Input: arr = [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: arr = [1,1,0,1,1]
Output: [-1,-1]
Example 3:

Input: arr = [1,1,0,0,1]
Output: [0,2]


Constraints:

3 <= arr.length <= 3 * 104
arr[i] is 0 or 1
"""
from typing import List


class ThreeEqualParts:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        IMPOSSIBLE = [-1, -1]
        n = len(arr)

        #要能平分成三个部分值都相等，每个部分的1必须一样多
        #To be equally divided into three parts with equal values, each part must have the same number of 1s
        #先记录下每个1的位置
        #Firstly, record the each 1's position
        mindex = [i for i in range(n) if arr[i] == 1]
        m = len(mindex)

        #None 1
        if m == 0:
            return [0, n-1]

        if m % 3 != 0:
            return IMPOSSIBLE

        #Divid 1s into three parts
        p1, p2 = mindex[0], mindex[m//3-1]
        p3, p4 = mindex[m//3], mindex[2*m//3-1]
        p5, p6 = mindex[2*m//3], mindex[-1]
        part1 = arr[p1: p2+1]
        part2 = arr[p3: p4+1]
        part3 = arr[p5: p6+1]

        if part1 != part2 or part1 != part3:
            return IMPOSSIBLE

        #1前面的0不影响值的大小，值的大小取决于最后的1后面的0的个数，所以最后的0的长度只能最小
        #The 0 in front of 1 does not affect the value of the array, the value of the array depends on the number of 0s after the last 1, so the length of the last 0 can only be the smallest
        lenZeroLeft = p3 - p2 - 1
        lenZeroMid = p5 - p4 - 1
        lenZeroTail = n - p6 - 1
        if lenZeroTail > lenZeroLeft or lenZeroTail > lenZeroMid:
            return IMPOSSIBLE

        return [p2+lenZeroTail, p4+lenZeroTail+1]
