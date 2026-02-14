# https://leetcode.com/problems/longest-balanced-substring-ii/submissions/1918430782

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        p = [[0, 0, 0]]
        for c in s:
            p.append(p[-1][:])
            p[-1]["abc".index(c)] += 1

        ans = 0
        m = {}
        for i, (a, b, c) in enumerate(p):
            for k in [
                (-1, a - b, a - c), # a,b,c
                (-2, a - b, c),     # a,b
                (-3, b - c, a),     # b,c
                (-4, c - a, b),     # a,c
                (-5, b, c),         # a
                (-6, c, a),         # b
                (-7, a, b),         # c
            ]:
                if not k in m: m[k] = i
                else: ans = max(ans, i - m[k])

        return ans

# 1. prefix sums of counts of a,b,c
# 2. for each prefix sum, we want to find the longest previous prefix sum with the same differences of counts (a-b, a-c)
# 3. we also want to consider the cases where we only care about a,b or a,c or b,c or just a or just b or just c
# the key is to use a dictionary to store the earliest index of each prefix sum configuration
# time complexity: O(n)
# space complexity: O(n) in the worst case, but typically O(1) since there are only a limited number of configurations of differences.