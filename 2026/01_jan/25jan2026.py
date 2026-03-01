# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/submissions/1895838429

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        ans = float('inf')
        for i in range(n):
            last_element = (i + k - 1)
            if last_element >= n:
                break
            
            ans = min(ans, nums[last_element] - nums[i])
        
        return ans
