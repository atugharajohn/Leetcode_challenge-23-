# problem:
# https://leetcode.com/problems/linked-list-random-node/

# solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        reservoir = self.head.val
        
        i = 2
        next = self.head.next
        while next:
            if random.random() < 1/i:
                reservoir = next.val
                
            i += 1
            next = next.next
            
        return reservoir