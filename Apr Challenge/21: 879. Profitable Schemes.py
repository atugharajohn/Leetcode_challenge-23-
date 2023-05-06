# problem:
# https://leetcode.com/problems/profitable-schemes/

# solution:
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i, members, cur_profit):
            if i >= len(profit):
                if cur_profit >= minProfit and members <= n:
                    return 1
                else:
                    return 0 
            ans = 0
            ans += dfs(i + 1, members, cur_profit)
            if members + group[i] <= n:
                ans += dfs(i + 1, members + group[i], min(cur_profit + profit[i], minProfit))
            return ans
        return dfs(0, 0, 0) % (10**9 + 7)
        