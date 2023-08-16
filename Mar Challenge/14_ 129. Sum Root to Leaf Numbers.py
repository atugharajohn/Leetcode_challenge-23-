# problem:
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# solution:
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        n_sum = 0
        def dfs(n, num):
            nonlocal n_sum
            for c in [n.left, n.right]:  # try to go deeper to one of the descendants
                if c:
                    dfs(c, num*10 + n.val)
            if not n.left and not n.right:  # leaf node
                n_sum += num*10 + n.val
        dfs(root, 0)
        return n_sum