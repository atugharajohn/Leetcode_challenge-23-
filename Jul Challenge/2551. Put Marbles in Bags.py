# problem:
# https://leetcode.com/problems/put-marbles-in-bags/

# solution:
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = sorted(map(sum,(pairwise(weights))))
        return sum(arr[-k+1:]) - sum(arr[:k-1]) if k > 1 else 0
        