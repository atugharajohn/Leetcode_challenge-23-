# problem:
# https://leetcode.com/problems/maximize-score-after-n-operations/

# solution:
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b:
                a,b = b,a % b
            return a
        @lru_cache(None)
        def dp(step,mask):
            if mask == (1<<n - 1):
                return 0
            ans = 0
            for i in range(n):
                if mask & (1<<i) == 0:
                    for j in range(i+1,n):
                        if mask & (1 << j) == 0:
                            ans = max(ans,step*gcd(nums[i],nums[j])+dp(step+1,mask |(1<<i)|(1<<j)))
            return ans
        n = len(nums)
        return dp(1,0)