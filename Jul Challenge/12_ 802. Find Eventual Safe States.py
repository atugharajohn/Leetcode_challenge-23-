# problem:
# https://leetcode.com/problems/find-eventual-safe-states/

# solution:
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n=len(graph)
        safe={}
        ans=[]
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i]=True
            return safe[i]

        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans                      
        