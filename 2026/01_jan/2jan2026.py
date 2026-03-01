# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/1871475018

from collections import defaultdict

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        buffer = defaultdict(int)
        for n in nums:
            buffer[n] += 1
            if buffer[n] > 1:
                return n