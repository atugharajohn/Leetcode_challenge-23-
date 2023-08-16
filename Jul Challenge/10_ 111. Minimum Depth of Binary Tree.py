# problem:
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else min(self.minDepth(root.left), self.minDepth(root.right)) + 1 if root.left and root.right else max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        