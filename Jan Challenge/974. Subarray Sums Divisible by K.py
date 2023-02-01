# problem:
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

# solution:
from itertools import accumulate

class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        m, tot = [1] + [0 for i in range(k - 1)], 0
        
        for i in accumulate(nums):
            tot += m[i%k]
            m[i%k] += 1
        
        return tot

