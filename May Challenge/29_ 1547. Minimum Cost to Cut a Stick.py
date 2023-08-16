# problem:
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

# solution:
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cache = {}
        def dfs(lower,upper, i , j):
            if j-i == 0:
                return 0
            if (lower, upper) in cache:
                return cache[(lower, upper)]
            ans = float("inf")
            for k in range(i, j):
                a = dfs(lower,cuts[k], i,k)
                b = dfs(cuts[k], upper, k+1, j)
                ans = min(ans, a+b)
            cache[(lower, upper)] = ans + (upper - lower)
            return ans + (upper - lower)
        return dfs(0,n,0, len(cuts))
