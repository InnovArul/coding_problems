# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/submissions/1933801961

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        currsum = 0
        
        for i in range(n+1):
            curr_bin_str = (bin(i)[2:]).lstrip("0")
            currshift = len(curr_bin_str)
            currsum = (((currsum << currshift) % MOD) + (i % MOD)) % MOD
        
        return currsum

# Time complexity: O(n log n) due to the conversion of integers to binary strings
# Space complexity: O(1) since we are using a constant amount of space for the variables
