# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/submissions/1911225896

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_suffix = [0] * n
        a_suffix[-1] += (s[-1] == 'a')

        b_prefix = [0] * n
        b_prefix[0] += (s[0] == 'b')

        # calculate b prefix sum
        for i in range(1, n):
            b_prefix[i] = (s[i] == 'b') + b_prefix[i-1]

        # calculate a suffix sum
        for i in range(n-2, -1, -1):
            a_suffix[i] = (s[i] == 'a') + a_suffix[i+1]

        min_deletions = float('inf')
        for i in range(n):
            min_deletions = min(min_deletions, (a_suffix[i+1] if i < n-1 else 0) + 
                                                (b_prefix[i-1] if i > 0 else 0))

        return min_deletions

# Time Complexity: O(n)
# Space Complexity: O(n)