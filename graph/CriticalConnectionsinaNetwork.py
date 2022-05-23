"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]


Constraints:

2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from typing import List


class CriticalConnectionsinaNetwork:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ans = []
        visitimes = [0]*n #traveral all map pass the point times
        minitimes = [0]*n #mininum times
        neighbors = {}

        #construct the connection map graph
        for node, neighbor in connections:
            if node not in neighbors:
                neighbors[node] = []
            neighbors[node].append(neighbor)
            if neighbor not in neighbors:
                neighbors[neighbor] = []
            neighbors[neighbor].append(node)

        def dfs(node: int, parent: int, time: int) -> None:
            visitimes[node] = time
            minitimes[node] = time
            for nghb in neighbors[node]:
                if nghb == parent:
                    continue  #skip the parent point
                if visitimes[nghb] == 0:  #no visited
                    dfs(nghb, node, time+1)

                minitimes[node] = min(minitimes[node], minitimes[nghb])
                if visitimes[node] < minitimes[nghb]:
                    ans.append([node, nghb])

        dfs(0, -1, 1)
        return ans

ccn = CriticalConnectionsinaNetwork()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
ans = ccn.criticalConnections(n, connections)
print(ans)


