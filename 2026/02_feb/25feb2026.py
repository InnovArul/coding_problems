# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/submissions/1930567701

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr, key=lambda x: (bin(x)[2:].count('1'), x))
        return arr

# Time complexity: O(n log n) due to sorting
# Space complexity: O(n) for the sorted array
