# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/submissions/1878114377

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.maxsum = -float("inf")
        self.totalsum = 0
        
        def subtreeSum(node):
            if not node: 
                return 0
            currSubtreeSum = node.val + subtreeSum(node.left) + subtreeSum(node.right)
            self.maxsum = max(self.maxsum, currSubtreeSum * (self.totalsum - currSubtreeSum))
            return currSubtreeSum

        self.totalsum = subtreeSum(root)
        subtreeSum(root)
        return self.maxsum % 1_000_000_007