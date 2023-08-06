# problem:
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def makeparent(self,node,parent):
        if node is None:
            return 
        node.parent=parent
        self.makeparent(node.left,node)
        self.makeparent(node.right,node)
    
    def trav(self,node,dist):
        if node is None or node in self.seen:
            return 
        self.seen.add(node)
        if dist==self.k:
            self.ans.append(node.val)
            return
        self.trav(node.parent,dist+1)
        self.trav(node.left,dist+1)
        self.trav(node.right,dist+1)
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.k=k
        self.makeparent(root,None)
        self.seen=set()
        self.ans=[]
        self.trav(target,0)
        return self.ans
        