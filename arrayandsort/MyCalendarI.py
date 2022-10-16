"""
MyCalendarI
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:

0 <= start < end <= 10^9
At most 1000 calls will be made to book.
"""
from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        #self.calendar = []
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        """
        def binary_search(x: int) -> int:
            l, r = 0, len(self.calendar)-1
            while l <= r:
                mid = (l+r) // 2
                if self.calendar[mid][0] == x:
                    return mid
                elif self.calendar[mid][0] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        """

        #idx = binary_search(end)
        idx = bisect_left(self.starts, end)
        if idx == 0:
            #self.calendar.insert(0, [start, end])
            self.starts.insert(0, start)
            self.ends.insert(0, end)
            return True
        else:
            if start >= self.ends[idx-1]: #self.calendar[idx-1][1]:
                #self.calendar.insert(idx, [start, end])
                self.starts.insert(idx, start)
                self.ends.insert(idx, end)
                return True
            else:
                return False


