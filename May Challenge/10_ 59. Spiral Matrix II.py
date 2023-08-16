# problem:
# https://leetcode.com/problems/spiral-matrix-ii/

# solution:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        i, r, c = 1, 0, 0

        while i <= n**2:
            while r < n and ans[c][r] == 0:
                ans[c][r] = i
                r += 1 if r != n-1 and ans[c][r+1] == 0 else 0
                i += 1
            c += 1

            while c < n and ans[c][r] == 0:
                ans[c][r] = i
                c += 1 if c != n-1 and ans[c+1][r] == 0 else 0
                i += 1
            r -= 1

            while r >= 0 and ans[c][r] == 0:
                ans[c][r] = i
                r -= 1 if r != 0 and ans[c][r-1] == 0 else 0
                i += 1
            c -= 1

            while c >= 0 and ans[c][r] == 0:
                ans[c][r] = i
                c -= 1 if c != 0 and ans[c-1][r] == 0 else 0
                i += 1
            r += 1

        return ans