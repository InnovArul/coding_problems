# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = nums[0] + nums[-1]
        n = len(nums)
        for a, b in zip(nums[:n//2], reversed(nums[n//2:])):
            ans = max(ans, a+b)
        
        return ans
