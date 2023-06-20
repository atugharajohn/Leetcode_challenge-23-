# problem:
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

# solution:
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        @cache
        def dfs(node):
            if manager[node]==-1:
                return informTime[node]
            return informTime[node]+dfs(manager[node])

        ans=0
        for i in range(n):
            ans=max(ans,dfs(i))
        return ans