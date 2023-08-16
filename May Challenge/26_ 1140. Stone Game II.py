# problem:
# https://leetcode.com/problems/stone-game-ii/

# solution:
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        @cache
        def dp(i,m):
            if i >= l :
                return 0
            val = max(sum(piles[i:]) - dp(i+x,max(x,m)) for x in range(1, (2*m) + 1))
            return val
        return dp(0,1)
