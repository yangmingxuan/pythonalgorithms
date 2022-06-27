"""

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.



Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation:
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0


Constraints:

1 <= courses.length <= 10^4
1 <= durationi, lastDayi <= 10^4
"""
from heapq import heappush, heappop
from typing import List


class CourseScheduleIII:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        courses.sort(key=lambda x:x[1])
        n, lastestTime = len(courses), courses[-1][1]
        dp = [[-1] * (lastestTime+1) for _ in range(n)]

        def schedule(idx: int, time: int) -> int:
            if idx == n:
                return 0
            if dp[idx][time] != -1:
                return dp[idx][time]

            attend = 0
            if time + courses[idx][0] <= courses[idx][1]:
                attend = 1 + schedule(idx+1, time+courses[idx][0])
            absent = schedule(idx+1, time)
            dp[idx][time] = max(attend, absent)
            return dp[idx][time]

        return schedule(0, 0)
        """
        courses.sort(key=lambda x: x[1])
        time = 0
        pg = []

        def insertPriorityIndex(item: int) -> int:
            l, r = 0, len(pg)-1
            while l <= r:
                mid = (l+r) // 2
                if pg[mid] == item:
                    return mid
                elif pg[mid] < item:
                    l += 1
                else:
                    r -= 1
            return l

        for c in courses:
            if time + c[0] <= c[1]:
                time += c[0]
                idx = insertPriorityIndex(c[0])
                pg.insert(idx, c[0])
            elif pg and pg[-1] > c[0]: #get the max course time
                time += c[0] - pg.pop() #attend this course and miss max time course
                idx = insertPriorityIndex(c[0])
                pg.insert(idx, c[0]) #attend this course

        return len(pg)

    def scheduleCourse2(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time = 0
        pg = []

        for t, end in courses:
            time += t
            heappush(pg, -t)
            while time > end:
                time += heappop(pg)

        return len(pg)
