# https://leetcode.com/problems/max-dot-product-of-two-subsequences/submissions/1879097020

from functools import cache
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def subsum(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0

            use_current_multiply = nums1[i] * nums2[j]
            return max(use_current_multiply + subsum(i+1, j+1),
                       subsum(i+1, j+1), # dont use current indices i, j
                       subsum(i, j+1),
                       subsum(i+1, j)
                    )
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        return subsum(0, 0)