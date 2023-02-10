# problem:
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q=[root]
        while q:
            t = q.pop()
            res.append(t.val)
            if t.right:
                q.append(t.right)
            if t.left:
                q.append(t.left)
        return res