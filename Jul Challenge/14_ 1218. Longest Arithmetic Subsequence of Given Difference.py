# problem:
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

# solution:
from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = []
        hash = defaultdict(int)
        for e in arr:
            res.append(1+hash[e-difference])
            hash[e] = 1+hash[e-difference]

        return max(res)
        