# problem:
# https://leetcode.com/problems/longest-arithmetic-subsequence/

# solution:
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n

        longest = 2
        dp = [{} for _ in range(n)] # List of dictionaries

        for i in range(n):
            for j in range(i):
                # Get diff
                diff = nums[i] - nums[j]

                # Set subsequence length (with d = diff) = prev + 1 (set 2 in prev not exist)
                dp[i][diff] = dp[j].get(diff, 1) + 1

                # Update longest subsequence
                longest = max(longest, dp[i][diff])

        return longest