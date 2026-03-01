# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field

from itertools import combinations

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7

        hf = [1] + sorted(hFences) + [m]
        vf = [1] + sorted(vFences) + [n]

        hf_set = set()
        for i, j in combinations(hf, 2):
            diff = abs(i-j)
            hf_set.add(diff)
        
        side = -1
        for i, j in combinations(vf, 2):
            diff = abs(i-j)
            if diff in hf_set:
                side = max(side, diff)

        if side > 0:
            return int((side * side) % mod)
        else: return -1