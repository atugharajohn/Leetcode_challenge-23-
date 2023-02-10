# problem:
# https://leetcode.com/problems/delete-columns-to-make-sorted/

# solution:
class Solution:
    def minDeletionSize(self, l: List[str]) -> int:
        l = list(map(list,zip(*l)))
        c = 0
        for i in l:
            if i!=sorted(i):
                c+=1
        return c