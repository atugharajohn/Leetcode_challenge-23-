# problem:
# https://leetcode.com/problems/predict-the-winner/

# solution:
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1: return True

        @cache
        def recurse(l, r):
            if l==r:
                return nums[l]
            return max(nums[l]-recurse(l+1, r), nums[r]-recurse(l, r-1))
        return recurse(0, n-1)>=0