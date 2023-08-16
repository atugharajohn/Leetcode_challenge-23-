# problem:
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

# solution:
class Solution:
    MOD = 10**9 + 7
    
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        apple = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                apple[i][j] = apple[i+1][j] + apple[i][j+1] - apple[i+1][j+1] + (pizza[i][j] == 'A')
        
        dp = {}
        def solve(i, j, p):
            if (i, j, p) in dp:
                return dp[(i, j, p)]
            if p == 1:
                return 1 if apple[i][j] > 0 else 0
            ans = 0
            for r in range(i+1, m):
                if apple[i][j] - apple[r][j] > 0:
                    ans = (ans + solve(r, j, p-1)) % self.MOD
            for c in range(j+1, n):
                if apple[i][j] - apple[i][c] > 0:
                    ans = (ans + solve(i, c, p-1)) % self.MOD
            dp[(i, j, p)] = ans
            return ans
        
        return solve(0, 0, k)