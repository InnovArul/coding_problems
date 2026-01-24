# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/submissions/1876960298

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        currlevel = [root]
        maxsum = -float("inf")
        maxsumlevel = None
        level = 0
        while currlevel:
            currsum = 0
            nextlevel = []
            level += 1
            for node in currlevel:
                currsum += node.val
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            
            if currsum > maxsum:
                maxsum = currsum
                maxsumlevel = level
            
            currlevel = nextlevel
        
        return maxsumlevel