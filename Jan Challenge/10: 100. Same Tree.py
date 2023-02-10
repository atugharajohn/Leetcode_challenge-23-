# problem:
# https://leetcode.com/problems/same-tree/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p ==None or q == None):
            if p==q: return True
            return False
        p_qu = [p]
        q_qu = [q]
        while p_qu and q_qu:
            t1 = p_qu.pop()
            t2 = q_qu.pop()
            if t1.val != t2.val: return False
            if t1.left and t2.left==None or t1.left == None and t2.left:
                return False
            if t1.right and t2.right==None or t1.right == None and t2.right:
                return False
            if t1.left: p_qu.append(t1.left)
            if t2.left: q_qu.append(t2.left)
            if t1.right: p_qu.append(t1.right)
            if t2.right: q_qu.append(t2.right)
        if p_qu != q_qu: return False
        return True