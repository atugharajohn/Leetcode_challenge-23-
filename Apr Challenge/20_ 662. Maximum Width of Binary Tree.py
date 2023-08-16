# problem:
# https://leetcode.com/problems/maximum-width-of-binary-tree/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lvls = []

        def helper(node, lvl, num):
            if not node:
                return

            if len(lvls) == lvl:
                lvls.append([float('+inf'), 0])

            lvls[lvl][0] = min(lvls[lvl][0], num)
            lvls[lvl][1] = max(lvls[lvl][1], num)

            helper(node.left, lvl + 1, num * 2)
            helper(node.right, lvl + 1, num * 2 + 1)

        helper(root, 0, 0)

        return max(lvl[1] - lvl[0] + 1 for lvl in lvls)