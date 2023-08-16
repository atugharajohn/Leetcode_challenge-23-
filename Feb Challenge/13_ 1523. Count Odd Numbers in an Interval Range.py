# problem:
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# solution:
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low+high%2+low%2)//2