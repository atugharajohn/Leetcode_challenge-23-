# problem:
# https://leetcode.com/problems/symmetric-tree/

# solution:
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        return isMirror(root.left, root.right)