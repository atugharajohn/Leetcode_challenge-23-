# problem:
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

# solution:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = prev = curr = 0

        for bit in nums:
            if bit:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0

        return longest - (longest == len(nums))