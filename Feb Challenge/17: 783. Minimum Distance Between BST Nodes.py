# problem:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# solution:
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        best = float('inf')
        last = float('inf')

        def dfs(node):
            nonlocal last, best
            if node:
                dfs(node.left)
                best, last = min(best, abs(last - node.val)), node.val
                dfs(node.right)

        dfs(root)
        return best