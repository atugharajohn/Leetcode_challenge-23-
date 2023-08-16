# problem:
# https://leetcode.com/problems/search-insert-position/

# solution:
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m]==target: return m
            if target<nums[m]: h = m-1
            else: l = m+1
        return (l+h)//2+1