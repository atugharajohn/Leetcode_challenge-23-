# problem:
# https://leetcode.com/problems/evaluate-division/

# solution:
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        visited=set()
        v=[]
        
        def answer(current, end, scalar):
            if current==end: 
                return scalar
            visited.add(current)
            if current in graph:
                for i in graph[current]:
                    if i[0] not in visited:
                        a=answer(i[0],end,scalar*i[1])
                        if a!=-1: 
                            return a
            return -1
        
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]]=[]
            if equations[i][1] not in graph:
                graph[equations[i][1]]=[]
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))

        for i in queries:
            visited=set()
            if i[0] not in graph or i[1] not in graph:
                v.append(-1)
                continue
            v.append(answer(i[0],i[1],1) if i[0]!=i[1] else 1)
        return v