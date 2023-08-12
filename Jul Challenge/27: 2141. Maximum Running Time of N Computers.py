# problem:
# https://leetcode.com/problems/maximum-running-time-of-n-computers/

# solution:
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        pool = 0
        l = len(batteries) - n
        res = batteries[l]
        for i, v in enumerate(batteries):
            if i < l:
                pool += v
            elif v != res:
                if pool >= (v - res) * (i - l):
                    pool -= (v - res) * (i - l)
                    res = v
                else :
                    return res + pool // (i - l)
        return res + pool // n
