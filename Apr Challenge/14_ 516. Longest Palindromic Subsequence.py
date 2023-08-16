# problem:
# https://leetcode.com/problems/longest-palindromic-subsequence/

# solution:
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def dp(l: int, r: int) -> int:
            if l == r: return 1
            if r < l: return 0
            if s[l] == s[r]:
                return 2 + dp(l+1, r-1)
            return max(dp(l+1, r), dp(l, r-1))
        # end dp()

        if s == s[::-1]: return len(s)
        
        return dp(0, len(s)-1)
