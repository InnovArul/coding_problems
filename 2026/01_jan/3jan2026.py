# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/submissions/1873582687

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        A = 6  # all different
        B = 6  # first == third

        for _ in range(2, n + 1):
            newA = (2 * A + 2 * B) % MOD
            newB = (2 * A + 3 * B) % MOD
            A, B = newA, newB

        return (A + B) % MOD