# problem:
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

# solution:
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 1:
                return 1
            else:
                r = [n for n in nums[1:] if n > nums[0]]
                l = [n for n in nums[1:] if n < nums[0]]
                return comb(len(r)+len(l), len(r))*f(l)*f(r)
        return (f(nums)-1) % (10**9 + 7)
