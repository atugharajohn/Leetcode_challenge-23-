# problem:
# https://leetcode.com/problems/number-of-provinces/

# solution:
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dic = {}
        for i in range(len(isConnected)):
            dic.setdefault(i, [])
            for j in range(len(isConnected[i])):
                dic.setdefault(j, [])
                if isConnected[i][j] == 1:
                    dic[i].append(j)
                    dic[j].append(i)
        visited = set()
        def dfs(cur):
            if len(dic[cur]) == 0:
                return
            if cur in visited:
                return
            visited.add(cur)
            for c in dic[cur]:
                dfs(c)
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count+=1
        return count