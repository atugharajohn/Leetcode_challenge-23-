# problem:
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

# solution:
class Solution:
    def distanceLimitedPathsExist(self, n: int, edg: List[List[int]], que: List[List[int]]) -> List[bool]:
        def getPar(v,par):
            if v==par[v]:
                return par[v]
            return getPar(par[v],par)

        def union(u,v,rank,par):
            u=getPar(u,par)
            v=getPar(v,par)
            if rank[u]<rank[v]:
                par[u]=v
            elif rank[v]<rank[u]:
                par[v]=u
            else:
                par[v]=u
                rank[u] += 1
            
          
        l=len(que)
        el=len(edg)
        for i in range(l):
            que[i].append(i)
        edg.sort(key=lambda x:x[2])
        que.sort(key=lambda x:x[2])
        par=[i for i in range(n)]
        rank=[0 for i in range(n)]
        ans=[False for i in range(l)]
        i,j=0,0
        while i<l:
            while j<el and edg[j][2]<que[i][2]:
                union(edg[j][0],edg[j][1],rank,par)
                j += 1
            src= getPar(que[i][0],par)
            dest=getPar(que[i][1],par)  
            if src==dest:
                ans[que[i][3]]=True
            i += 1
        return ans