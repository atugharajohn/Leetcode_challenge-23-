# problem:
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ele=[]
        while head:
            ele+=[head.val]
            head=head.next
        n=len(ele)
        k=0
        for i in range(len(ele)//2+1):
            count=ele[i]+ele[n-1-i]
            if count>k:
                k=count
        return k