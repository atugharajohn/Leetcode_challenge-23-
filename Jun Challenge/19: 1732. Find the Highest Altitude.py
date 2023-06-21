# problem:
# https://leetcode.com/problems/find-the-highest-altitude/

# solution:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=0
        m=0
        for i in gain:
            n+=i
            m=max(n,m)
        return m
