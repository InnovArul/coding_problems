# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/submissions/1903712338

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minsum = nums[0]

        # find 2 small numbers from remaining list
        rem = nums[1:]
        rem.sort()
        minsum += rem[0]
        minsum += rem[1]

        return minsum
    
# Time Complexity: O(n log n) due to sorting the remaining list
# Space Complexity: O(1) if we ignore the space used for sorting