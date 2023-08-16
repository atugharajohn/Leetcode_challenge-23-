# problem:
# https://leetcode.com/problems/similar-string-groups/

# solution:
class Solution:
    def are_neighbors(self, s1, s2):
        mismatches = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                mismatches += 1
        return mismatches<3

    def numSimilarGroups(self, strs: List[str]) -> int:
        seen = set()
        res = 0
        for k in range(len(strs)):
            if k in seen:
                continue
            
            res += 1
            q = [k]
            seen.add(k)

            while q:
                i = q.pop()
                for j in range(len(strs)):
                    if i!=j and j not in seen and self.are_neighbors(strs[i], strs[j]):
                        q.append(j)
                        seen.add(j)
        
        return res
            

