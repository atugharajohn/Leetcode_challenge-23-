# problem:
# https://leetcode.com/problems/jump-game-ii/

# solution:
class Solution:
    def jump(self, nums: List[int]) -> int:
        d = defaultdict(set)
        d[0].add(0)
        for i,n in enumerate(nums[:-1]):
            curr = min(d[i]) + 1
            for j in range(1, n+1):
                d[i+j].add(curr)
            del d[i]
        return min(d[len(nums)-1])