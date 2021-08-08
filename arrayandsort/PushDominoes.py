"""
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""

class PushDominoes:
    """
     * Explanation: 从左往右标上右向的正值，再从右往左标上左向的负值，最终为正值的倒向右，负值倒向左，0为不动。
     * From left to right, mark the positive value to the right, and then mark the negative value to the left from right to left, and finally the positive value is reversed to the right, the negative value is reversed to the left, and 0 means no movement.
    """
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        directions = [0] * n

        direction = 0
        #from left to right
        for i in range(n):
            if dominoes[i] == 'R':
                direction = n
            elif dominoes[i] == 'L':
                direction = 0
            else:
                direction -= 1
                direction = max(direction, 0)
            directions[i] += direction

        direction = 0
        #from right to left
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                direction = n
            elif dominoes[i] == 'R':
                direction = 0
            else:
                direction -= 1
                direction = max(direction, 0)
            directions[i] -= direction

        ans = ""
        for i in range(n):
            ans += 'R' if directions[i] > 0 else 'L' if directions[i] < 0 else '.'

        return ans

    def pushDominoes2(self, dominoes: str) -> str:
        n = len(dominoes)
        buff_count = 0
        isinright = False

        ans = ""
        for ch in dominoes:
            if ch == '.':
                buff_count += 1
            elif ch == 'R':
                if isinright:
                    ans += 'R' * buff_count
                else:
                    ans += '.' * buff_count
                    isinright = True
                buff_count = 1
            else:   #ch == 'L'
                if isinright:
                    s, y = divmod(buff_count+1, 2)
                    ans += 'R' * s + '.' if y == 1 else '' + 'L' * s
                    isinright = False
                else:
                    ans += 'L' * (buff_count+1)
                buff_count = 0

        if buff_count > 0:
            if isinright:
                ans += 'R' * buff_count
            else:
                ans += '.' * buff_count

        return ans
