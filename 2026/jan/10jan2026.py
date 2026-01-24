# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/submissions/1880880370

from functools import cache
import numpy as np

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def get_ascii_sum(string):
            ascii_sum = 0
            for c in string:
                ascii_sum += ord(c)

            return ascii_sum

        def print_ord(s):
            for c in s:
                print(c, ord(c))

        # print_ord(s1)
        # print_ord(s2)

        l1, l2 = len(s1), len(s2)
        dp = np.zeros((l1, l2))
        
        s1_sum = get_ascii_sum(s1)
        s2_sum = get_ascii_sum(s2)
        for i in range(0, l1):
            for j in range(0, l2):
                # dp[i, j] holds the max sum between s1[:i], s2[:j]
                if s1[i] == s2[j]:
                    dp[i, j] = get_ascii_sum(s2[j])
                    if i > 0 and j > 0:
                        dp[i, j] += dp[i-1, j-1]
                else:
                    # print(f" {i} {j} not equal")
                    dont_use_s1_cost = 0
                    if i > 0:
                        dont_use_s1_cost += dp[i-1, j]
                    
                    dont_use_s2_cost = 0
                    if j > 0:
                        dont_use_s2_cost += dp[i, j-1]
                    
                    dont_use_both_cost = 0
                    if i > 0 and j > 0:
                        dont_use_both_cost += dp[i-1, j-1]

                    dp[i, j] = max(dont_use_s1_cost, dont_use_s2_cost, dont_use_both_cost)

            # print(dp[i])
            # print("******")

        return int(s1_sum + s2_sum - 2 * dp[-1, -1])