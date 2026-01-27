# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [float('inf')] * n
        E = defaultdict(list)
        for i, j, w in edges:
            E[i].append((j, w))
            E[j].append((i, 2*w))

        dist[0] = 0
        q = [(0, 0)]
        while q:
            d, i = heapq.heappop(q)
            for index, w in E[i]:
                currdist = d + w
                if dist[index] > currdist:
                    dist[index] = currdist
                    heapq.heappush(q, (currdist, index))

        return -1 if dist[-1] == float('inf') else dist[-1]

# Time Complexity: O(E log V) where E is the number of edges and V is the number of vertices.
# Space Complexity: O(V + E) for the adjacency list and distance array.