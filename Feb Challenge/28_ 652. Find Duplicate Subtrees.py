# problem:
# https://leetcode.com/problems/find-duplicate-subtrees/

# solution:
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        hmap = defaultdict(int)
        res = []
        def dfs(node):
            if not node: return ''
            l, r = dfs(node.left), dfs(node.right)
            struct = f'l{l}{node.val}{r}r'
            hmap[struct] += 1
            if hmap[struct] == 2:
                res.append(node)
            return struct
        dfs(root)
        return res 