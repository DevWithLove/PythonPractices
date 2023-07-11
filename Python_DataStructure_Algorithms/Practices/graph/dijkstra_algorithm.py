"""
743. Network Delay Time
Medium

Companies
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


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
# network delay time - leetcode
from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        g = defaultdict(list)
        for u, v, cost in times:
            g[u].append((cost, v))

        # cost,node
        min_heap = [(0, K)]
        visited = set()
        distance = {i: float('inf') for i in range(1, N+1)}
        distance[K] = 0

        while min_heap:
            cur_dist, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            if len(visited) == N:
                return cur_dist

            for direct_distance, v in g[u]:
                if cur_dist + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_dist + direct_distance
                    heapq.heappush(min_heap, (cur_dist + direct_distance, v))
        return -1
