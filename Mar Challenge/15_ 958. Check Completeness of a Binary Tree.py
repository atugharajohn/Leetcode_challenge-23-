# problem:
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        result=[]
        queue=[root]
        while queue:
            curr=queue.pop(0)
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                return queue==[None]*len(queue)