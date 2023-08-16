# problem:
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

# solution:
class Solution:
    def LCS(self, s1: str, s2: str, m: int, n: int) -> int:
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    
    def minInsertions(self, s: str) -> int:
        # step-1 : find the longest palindromic subsequence(LPS)
        # step-2 : length(s)-length(LPS(s)) == answer
        n = len(s)
        s2 = s[::-1]
        s2[::-1]
        n = len(s)
        LPS_count = self.LCS(s,s2,n,n)
        return n - LPS_count