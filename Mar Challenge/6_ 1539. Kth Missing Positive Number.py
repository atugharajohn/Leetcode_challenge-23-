# problem:
# https://leetcode.com/problems/kth-missing-positive-number/

# solution:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x=1
        i=0
        j=1
        while True:
            while i<len(arr) and x==arr[i]:
                x+=1
                i+=1
            if j==k: return x
            x+=1
            j+=1