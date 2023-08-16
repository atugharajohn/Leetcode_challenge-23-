# problem:
# https://leetcode.com/problems/count-ways-to-build-good-strings/

# solution:
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        strCount = 0

        dp = [0]*(high+1)
        dp[0] = 1

        greater = max(zero,one)
        lesser = min(zero,one)

        for i in range(lesser,greater):
            dp[i] += dp[i-lesser]%(10**9 + 7)
        
        for i in range(greater,high+1):
            dp[i] += (dp[i-zero]+dp[i-one])%(10**9 + 7)
        
        return sum(dp[low:high+1])%(10**9 + 7)