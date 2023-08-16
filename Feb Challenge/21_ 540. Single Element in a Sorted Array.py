# problem:
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# solution:
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            try:
                if nums[i]!=nums[i+1]:
                    return nums[i]
            except: return nums[i]
            i+=2