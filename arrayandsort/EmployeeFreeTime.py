"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.



Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]


Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
"""

from arrayandsort import Interval


class EmployeeFreeTime:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        allschedule = []
        for employ in schedule:
            for interval in employ:
                allschedule.append(interval)

        allschedule.sort(key=lambda x: x.start)

        ans = []
        maxfreetime = 0
        for i in range(len(allschedule) - 1):
            maxfreetime = max(maxfreetime, allschedule[i].end)
            if allschedule[i].start == allschedule[i + 1].start:
                continue
            if maxfreetime < allschedule[i + 1].start:
                freetime = Interval(maxfreetime, allschedule[i + 1].start)
                ans.append(freetime)

        return ans
