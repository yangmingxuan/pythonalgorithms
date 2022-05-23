"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:

            1             1           1
    1<-------------2------------>3---------->4

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
from typing import List


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        miniTime = 0
        graph = {} #record each node's edges and delay time
        visited = {} #record visited node and minimum time to reach this node

        #construct the graph
        for node, nxtnode, time in times:
            if node not in graph:
                graph[node] = []
            graph[node].append((nxtnode, time))

        nq = []
        #put the start node into queue
        nq.append(k)
        visited[k] = 0

        while nq:
            node = nq.pop(0)
            if node in graph:
                for nxtnode, time in graph[node]:
                    if nxtnode not in visited or visited[node]+time < visited[nxtnode]:
                        #if not visited or get a shorter path
                        nq.append(nxtnode)
                        visited[nxtnode] = visited[node]+time

        if(len(visited) != n):
            return -1

        miniTime = max(visited.values())
        return miniTime
