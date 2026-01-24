# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/submissions/1880111210

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getMaxDepthAndTopNode(node, current_depth):
            if not node: 
                return current_depth, None

            # get child max depths
            left_depth, left_root = getMaxDepthAndTopNode(node.left, current_depth + 1)
            right_depth, right_root = getMaxDepthAndTopNode(node.right, current_depth + 1)
            if left_depth > right_depth:
                return left_depth, left_root
            elif left_depth < right_depth:
                return right_depth, right_root
            else:
                # left_depth == right_depth
                return left_depth, node

        max_depth, node = getMaxDepthAndTopNode(root, 0)
        return node