# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/submissions/1940255612

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev_one = -1
        if s[0] == '0': return False

        for i, c in enumerate(s):
            if c == '0': continue

            if c == '1':
                print(prev_one)
                if prev_one == -1 or prev_one == (i-1):
                    prev_one = i
                else:
                    return False

        return True

# Time complexity: O(n)
# Space complexity: O(1)
