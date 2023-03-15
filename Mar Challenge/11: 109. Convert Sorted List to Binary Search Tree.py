# problem:
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# solution:
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def binInsert(root,new_node):
            if not root: 
                root = new_node
            else:
                if new_node.val<root.val:
                    if root.left: 
                        root.left= binInsert(root.left,new_node)
                    else: root.left = new_node
                elif new_node.val>root.val:
                    if root.right: root.right = binInsert(root.right, new_node)
                    else: root.right = new_node
            return root
        while head:
            root = (None,TreeNode(head.val))
            head=head.next
        return root