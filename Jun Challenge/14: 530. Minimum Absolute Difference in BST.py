# problem:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans: int = float('inf')
        array: List[int] = []
        def f(node: TreeNode):
            if not node:
                return
            f(node.left)
            array.append(node.val)
            f(node.right)
        f(root)

        prev: int = array[0]
        for i in range(1, len(array)):
            num: int = array[i]
            ans = min(ans, num - prev)
            prev = num

        return ans