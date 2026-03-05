# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/submissions/1939065509

class Solution:
    def minOperations(self, s: str) -> int:
        length = len(s) + 1
        str_to_check = '01' * (length // 2)

        if len(s) % 2 == 0:
            str_to_check += '0'

        start0 = str_to_check[:-1]
        start1 = str_to_check[1:]

        def check_flip(str1, str2):
            return sum([0 if p == q else 1 for p, q in zip(str1, str2)])

        return min(check_flip(s, start0), check_flip(s, start1))

# Time complexity: O(n)
# Space complexity: O(n)
