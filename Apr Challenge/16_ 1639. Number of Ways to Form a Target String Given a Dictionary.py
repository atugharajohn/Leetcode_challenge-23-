# problem:
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

# solution:
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        mod = 10**9 + 7
        dp = [0] * (m+1)
        dp[0] = 1
        
        count = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for word in words:
                count[i][ord(word[i]) - ord('a')] += 1
        
        for i in range(n):
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * count[i][ord(target[j]) - ord('a')]
                dp[j+1] %= mod
        
        return dp[m]