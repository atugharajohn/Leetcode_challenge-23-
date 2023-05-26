# problem:
# https://leetcode.com/problems/new-21-game/

# solution:
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [1.0] + [0] * n
        Wsum = 1.0
        if k == 0 or n >= k + maxPts:
            return 1
        for i in range(1, n+1):
            dp[i] = Wsum/maxPts
            if i < k:
                Wsum += dp[i]
            if i >= maxPts:
                Wsum -= dp[i-maxPts]
        return sum(dp[k:])