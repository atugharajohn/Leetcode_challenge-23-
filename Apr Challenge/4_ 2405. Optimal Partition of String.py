# problem:
# https://leetcode.com/problems/optimal-partition-of-string/

# solution:
class Solution:
    def partitionString(self, s: str) -> int:
        count=1
        a=""
        for i in s:
            if i in a:
                a=i
                count+=1
            else:
                a+=i
        return count