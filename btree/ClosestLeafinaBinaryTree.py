"""
Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""
import collections
from typing import Dict, List

from btree import TreeNode


class ClosestLeafinaBinaryTree:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        if not root.left and not root.right and root.val == k:
            return k
        graph: Dict[TreeNode, List[TreeNode]] = collections.defaultdict(list)
        def dfs(node: TreeNode, parent: TreeNode):
            if not node:
                return
            if parent:
                graph[parent].append(node)
                graph[node].append(parent)
            dfs(node.left, node)
            dfs(node.right, node)

        #treat BT as graph, parent and children node as its neighbor
        dfs(root, None)
        queue = []
        visited = set()
        for node in graph.keys():
            if node.val == k:
                queue.append(node)
                visited.add(node)
                if not node.left and not node.right:
                    return node.val
                break

        while queue:
            node = queue.pop(0)
            #meet the first leaf node, return the val
            if not node.left and not node.right:
                return node.val
            for nei in graph[node]:
                if not nei in visited:
                    queue.append(nei)
                    visited.add(nei)

        return 0
