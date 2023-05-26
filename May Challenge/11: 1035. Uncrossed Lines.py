# problem:
# https://leetcode.com/problems/uncrossed-lines/

# solution:
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
            n = len(nums1)
            m = len(nums2)
            dp = [[0 for i in range(n+1)] for j in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if nums1[j-1] == nums2[i-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[-1][-1]