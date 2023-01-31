# problem:
# https://leetcode.com/problems/maximum-ice-cream-bars/

# solution:
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in costs:
            if i<=coins:
                coins = coins-i
                c+=1
        return c