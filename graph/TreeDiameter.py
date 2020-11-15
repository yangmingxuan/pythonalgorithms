"""
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.



Example 1:
    0
  /  \
 1    2

Input: edges = [[0,1],[0,2]]
Output: 2
Explanation:
A longest path of the tree is the path 1 - 0 - 2.
Example 2:
  0--1
    / \
   2   4
  /     \
 3       5


Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation:
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.


Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""
from typing import List


class TreeDiameter:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = {}
        for a, b in edges:
            if not a in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)
            if not b in graph:
                graph[b] = [a]
            else:
                graph[b].append(a)


        def bfs(node: int):
            seen = set()
            level = -1
            farthest = 0
            queue = []
            queue.append(node)
            while queue:
                level += 1
                size = len(queue)
                for i in range(size):
                    val = queue.pop(0)
                    seen.add(val)
                    farthest = val
                    for nei in graph[val]:
                        if not nei in seen:
                            queue.append(nei)
            return level, farthest

        #find the farthest node from first node
        _, farthestChild = bfs(edges[0][0])

        #find the longest length from the farthest node
        longest, _ = bfs(farthestChild)
        return longest
