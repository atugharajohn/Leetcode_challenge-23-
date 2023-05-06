# problem:
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

# solution:
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p=1
        for i in nums:
            if i==0: return 0
            p*=i
        return p//abs(p)