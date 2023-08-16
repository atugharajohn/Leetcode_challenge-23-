# problem:
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# solution:
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxw = max(weights)
        def check(cap):
            cur = 0
            res = 1
            for w in weights:
                if cur + w > cap:
                    res += 1
                    cur = 0
                cur += w
            return res
        left, right = max(weights), sum(weights)
        while left < right:
            m = (left + right)//2
            if check(m) > days:
                left = m + 1
            else:
                right = m
        return left