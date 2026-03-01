# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/submissions/1934604773

class Solution:
    def minPartitions(self, n: str) -> int:
        ans = max([int(d) for d in n])
        return ans

# Time complexity: O(n) where n is the number of digits in the input string.
# Space complexity: O(1) since we are using a constant amount of space to store
