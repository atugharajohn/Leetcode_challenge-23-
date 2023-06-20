# problem:
# https://leetcode.com/problems/detonate-the-maximum-bombs/

# solution:
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        G=[[] for _ in bombs]
        for i, (xi,yi,ri) in enumerate(bombs):
            for j, (xj,yj,rj) in enumerate(bombs):
                if i<j:
                    dis=(xi-xj)**2 + (yi-yj)**2
                    if dis<= ri**2:
                        G[i].append(j)
                    if dis<= rj**2:
                        G[j].append(i)
        def dfs(x):
            ans=1
            seen={x}
            stack=[x]
            while stack:
                u = stack.pop()
                for v in G[u]:
                    if v not in seen:
                        ans+=1
                        seen.add(v)
                        stack.append(v)
            return ans
        return max(dfs(x) for x in range(len(bombs)))
        