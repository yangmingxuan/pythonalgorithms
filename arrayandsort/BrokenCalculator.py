"""

There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.



Example 1:

Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.


Constraints:

1 <= x, y <= 10^9
"""

class BrokenCalculator:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        if startValue >= target:
            return startValue - target

        ans = 0
        minNum, maxNum = startValue//2, target+(target-1)//2+1
        visited = set()
        visited.add(startValue)
        queue = []
        queue.append(startValue)

        while queue:
            nxtQueue = []
            for num in queue:
                num1 = num - 1
                num2 = num * 2
                if num1 == target or num2 == target:
                    return ans+1
                if num1 not in visited and minNum <= num1 <= maxNum:
                    nxtQueue.append(num1)
                if num2 not in visited and minNum <= num2 <= maxNum:
                    nxtQueue.append(num2)
            ans += 1
            queue = nxtQueue

        return ans
        """
        ans = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
                ans += 1
            else:
                target = (target+1)//2
                ans += 2

        return ans+startValue-target

