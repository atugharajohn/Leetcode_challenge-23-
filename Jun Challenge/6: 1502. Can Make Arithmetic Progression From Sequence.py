# problem:
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# solution:
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        diff = abs(arr[0] - arr[1])
        for i in range(2,n):
            d = abs(arr[i-1] - arr[i])
            if(d != diff):
                return False
        return True


