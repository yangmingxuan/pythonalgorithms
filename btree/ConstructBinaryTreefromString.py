"""
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.



Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]


Constraints:

0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.
"""
from btree import TreeNode


class ConstructBinaryTreefromString:
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        self.index = 0

        def helper() -> TreeNode:
            val, sign = 0, True
            if s[self.index] == '-':
                sign = False
                self.index += 1
            while self.index < len(s) and s[self.index].isdigit():
                val = val * 10 + int(s[self.index])
                self.index += 1

            if not sign:
                val = -val

            node = TreeNode(val)
            if self.index < len(s) and s[self.index] == '(':
                self.index += 1
                node.left = helper()
                if self.index < len(s) and s[self.index] == '(':
                    self.index += 1
                    node.right = helper()
            if self.index < len(s) and s[self.index] == ')':
                self.index += 1

            return node

        return helper()


