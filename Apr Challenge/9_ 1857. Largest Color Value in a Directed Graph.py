# problem:
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

# solution:
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src,dest in edges:
            adj[src].append(dest)
        
        #to return the max frequence of color in a path
        def dfs(node):
            if node in path:
                return float("inf")
            if node in visited:
                return 0

            visited.add(node)
            path.add(node)

            colorInd = ord(colors[node])  - ord('a')
            count[node][colorInd] = 1
            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max(count[node][c],count[nei][c] + (1 if c==colorInd else 0))
            path.remove(node)
            return max(count[node])


        visited,path=set(),set()
        n,ans=len(colors),0
        count = [[0]* 26 for i in range(n)]
        for i in range(n):
            ans=max(ans,dfs(i))
        return -1 if ans==float("inf") else ans