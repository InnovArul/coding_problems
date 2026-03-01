# https://leetcode.com/problems/count-binary-substrings/submissions/1924832525

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 0
        currbit = '0'

        ans = 0
        for c in s:
            if c == currbit:
                curr += 1
            else:
                ans += min(curr, prev)

                # interchange curr to prev and reinit curr
                prev = curr
                curr = 1
                currbit = c
        
        ans += min(curr, prev)
        return ans

# Space complexity: O(1)
# Time complexity: O(n)
