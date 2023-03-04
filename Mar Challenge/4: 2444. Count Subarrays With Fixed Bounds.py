# problem:
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

# solution:
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        leftBound = -1
        lastMin, lastMax = -1, -1
        count = 0
        
        for i in range(n):
            if nums[i] >= minK and nums[i] <= maxK:
                lastMin = i if nums[i] == minK else lastMin
                lastMax = i if nums[i] == maxK else lastMax
                count += max(0, min(lastMin, lastMax) - leftBound)
            else:
                leftBound = i
                lastMin = -1
                lastMax = -1
        
        return count