# https://leetcode.com/problems/transformed-array/submissions/1909606094

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            # find the target element
            q = (i + nums[i]) % n
            res.append(nums[q])
        
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)