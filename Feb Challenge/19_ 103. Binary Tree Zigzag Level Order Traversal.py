# problem:
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        q = [root]
        ans = []
        level = 0
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level%2 ==1:
                temp = temp[::-1]
            ans.append(temp)
            level+=1
        return ans