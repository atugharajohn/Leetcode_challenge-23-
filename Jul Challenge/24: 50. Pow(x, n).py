# problem:
# https://leetcode.com/problems/powx-n/

# solution:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n is positive or negative
        pos = n > 0
        
        n = abs(n)
        def sol(n, dp):
            if n == 0:
                return 1
            if n==1:
                if pos:
                    return x
                return 1/x
            
            if n in dp:
                return dp[n]
            
            if n%2 == 0:
                dp[n] = sol(n//2, dp) * sol(n//2, dp)
                return dp[n]
            else:
                dp[n] = sol(n//2, dp) * sol(n//2 + 1, dp)
                return dp[n]
        
        dp = {}
        return sol(n,dp)
        