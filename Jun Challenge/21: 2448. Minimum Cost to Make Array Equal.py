# problem:
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

# solution:
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def fcost(n):
            tot = 0
            for i in range(len(cost)):
                tot += (abs(n - nums[i]) * cost[i])
            return tot
        
        l = min(nums)
        r = max(nums)
        while l < r:
            mid = (l + r) // 2
            if fcost(mid) < fcost(mid+1):
                r = mid
            else:
                l = mid + 1
        return fcost(l)