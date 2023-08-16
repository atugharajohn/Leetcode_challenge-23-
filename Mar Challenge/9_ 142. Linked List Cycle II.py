# problem:
# https://leetcode.com/problems/linked-list-cycle-ii/

# solution:
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        x=head
        while head:
            if x in l:
                return x
            l.append(x)
            try:
                x=x.next
            except:
                break
        return None