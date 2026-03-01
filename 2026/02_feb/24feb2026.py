# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/1930067749

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def add_sum(node, prefix):
            nonlocal ans
            prefix += str(node.val)

            if node.left or node.right:
                # for non-leaf nodes, propagate prefix to its children
                if node.left: add_sum(node.left, prefix)
                if node.right: add_sum(node.right, prefix)
            else:
                # for leaf nodes, convert to decimal and add to ans
                ans += int(prefix, 2)

        add_sum(root, "")
        return ans

# Space complexity: O(h) where h is the height of the tree
# Time complexity: O(n) where n is the number of nodes in the tree
