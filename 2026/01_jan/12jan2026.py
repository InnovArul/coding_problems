# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        for i, pt in enumerate(points[1:], 1):
            prevpt = points[i-1]
            dx, dy = abs(prevpt[0] - pt[0]), abs(prevpt[1] - pt[1])
            total += max(dx, dy)
        
        return total