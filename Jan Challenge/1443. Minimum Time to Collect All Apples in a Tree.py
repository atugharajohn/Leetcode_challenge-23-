# problem:
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

# solution:
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        
        def dfs(node,par):
            
            res = 0
            for nei in tree[node]:
                if nei != par:
                    res += dfs(nei,node)
            
            if res or hasApple[node]:
                return res + 2

            return res

        return max(dfs(0,-1)-2, 0)