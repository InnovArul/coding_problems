# https://leetcode.com/problems/balanced-binary-tree/submissions/1912317977

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def checkDepth(node):
            nonlocal ans
            if not node:
                return 0

            ldepth = checkDepth(node.left)
            rdepth = checkDepth(node.right)
            ans = ans and (abs(ldepth - rdepth) <= 1)
            return 1 + max(ldepth, rdepth)

        checkDepth(root)
        return ans

# Time complexity: O(n) where n is the number of nodes in the tree. We visit each node once to calculate its depth and check if it's balanced.
# Space complexity: O(h) where h is the height of the tree. In the worst case (a completely unbalanced tree), the height can be equal to the number of nodes, leading

