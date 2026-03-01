# https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/1902680324

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        low = 0
        high = n - 1
        ans = -1

        while low < high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid

        if letters[high] > target:
            return letters[high]
        else:
            return letters[0]

# Time Complexity: O(log n)
# Space Complexity: O(1)