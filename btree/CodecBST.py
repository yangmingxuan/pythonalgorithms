"""
Serialize and Deserialize BST
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.



Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
"""
import sys
from typing import List

from btree.TreeNode import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def postorder(node: TreeNode) -> List[int]:
            return postorder(node.left) + postorder(node.right) + [node.val] if node else []
        return ','.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data or len(data) == 0:
            return None
        vallist = [int(x) for x in data.split(',') if x]

        def helper(lower=-sys.maxsize, upper=sys.maxsize) -> TreeNode:
            if not vallist or vallist[-1] < lower or vallist[-1] > upper:
                return None

            val = vallist.pop()
            node = TreeNode(val)
            node.right = helper(val, upper)
            node.left = helper(lower, val)
            return node

        return helper()
