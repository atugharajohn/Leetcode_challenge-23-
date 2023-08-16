# problem:
# https://leetcode.com/problems/course-schedule/

# solution:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {c:[] for c in range(numCourses)}

        for crs,pre in prerequisites:
            prereq[crs].append(pre)

        cycle = set()
        visited = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True
            
        