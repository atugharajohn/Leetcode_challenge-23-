# problem:
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 0
        max_level = 0
        max_sum = float('-inf')
        
        q = collections.deque()
        q.append(root)
        
        while q:
            level += 1
            curr_sum = 0
            
            for _ in range(len(q)):
                node = q.popleft()
                
                curr_sum += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_level = level
                
        return max_level
