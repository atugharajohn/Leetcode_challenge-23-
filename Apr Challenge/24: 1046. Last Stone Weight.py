# problem:
# https://leetcode.com/problems/last-stone-weight/

# solution:
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            y=stones.pop(-1)
            x=stones.pop(-1)
            if x!=y:
                stones.append(y-x)
            stones.sort()
        return stones[0] if len(stones)>=1 else 0