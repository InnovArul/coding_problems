# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/submissions/1937126738

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1: return "0"
        def get_len(p):
            return (2 ** p) - 1

        currlen = get_len(n)

        # 1 based index
        middle_element_index = (currlen // 2) + 1

        # "1" is the connecting element between substrings
        if middle_element_index == k: return "1"
        elif k < middle_element_index:
            return self.findKthBit(n-1, k)
        else:
            # reverse invert
            # same as invert reverse
            # calculate reversed index
            len_n_minus_1 = get_len(n-1)
            remaining_index = k - middle_element_index
            next_index = len_n_minus_1 - remaining_index + 1
            char = self.findKthBit(n-1, next_index)
            invchar = "0" if char == "1" else "1"

            return invchar

# Space Complexity: O(n) due to recursion stack
# Time Complexity: O(n) due to recursion depth and calculations at each step
