# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/submissions/1902687501

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        adj_list = defaultdict(list)
        for idx in range(len(original)):
            adj_list[original[idx]].append((cost[idx], changed[idx]))
        
        dfs = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for start in original:
            dfs[start][start] = 0
            pq = [(0, start)]
            visited = set()
            while pq:
                dist, vtx = heapq.heappop(pq)
                if vtx in visited:
                    continue
                visited.add(vtx)
                dfs[start][vtx] = dist
                for cost, child in adj_list[vtx]:
                    new_dist = dist + cost
                    if child not in visited and dfs[start][child] > new_dist:
                        heapq.heappush(pq, (new_dist, child))
        
        n = len(source)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        original_set = set(original)
        changed_set = set(changed)
        valid_lengths = set(len(s) for s in original_set)

        for i in range(n):
            if dp[i] == INF:
                continue

            if source[i] == target[i]:
                if dp[i] < dp[i + 1]:
                    dp[i + 1] = dp[i]

            for L in valid_lengths:
                if i + L > n:
                    continue

                s_sub = source[i:i + L]
                if s_sub not in original_set:
                    continue

                t_sub = target[i:i + L]
                cost_val = dfs[s_sub][t_sub]
                if cost_val < INF:
                    cand = dp[i] + cost_val
                    if cand < dp[i + L]:
                        dp[i + L] = cand
        return -1 if dp[n] == INF else dp[n]

# Time Complexity: O(n * m^2 + p log p) where n is the length of source string,
# m is the maximum length of strings in original and changed arrays,
# and p is the total number of edges in the graph constructed from original and changed arrays.
# Space Complexity: O(p + n) for the adjacency list, distance table, and dp array.