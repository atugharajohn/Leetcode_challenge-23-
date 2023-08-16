# problem:
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        l=0
        while temp:
            temp=temp.next
            l+=1
        end=(l-k)+1
        temp=head
        l=1
        while temp:
            if l==k:
                c=temp
            if l==end:
                d=temp
            temp=temp.next
            l+=1
        c.val,d.val=d.val,c.val
        return head