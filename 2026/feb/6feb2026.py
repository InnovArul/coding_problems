# https://leetcode.com/problems/minimum-removals-to-balance-array/submissions/1910639224

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = n
        right = 0
        for left in range(n):
            right = bisect.bisect_right(nums, k * nums[left])
            ans = min(ans, n - (right - left))

        return ans

# Time Complexity: O(n log n)
# Space Complexity: O(1)