# problem:
# https://leetcode.com/problems/naming-a-company/

# solution:
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        hashMap = collections.defaultdict(set)
        for w in ideas:
            hashMap[w[0]].add(w[1:])
        
        res = 0
        for char1 in hashMap:
            for char2 in hashMap:
                if char1 == char2:
                    continue
                intersect = 0

                for w in hashMap[char1]:
                    if w in hashMap[char2]:
                        intersect += 1
                
                distinct1 = len(hashMap[char1]) - intersect
                distinct2 = len(hashMap[char2]) - intersect

                res += distinct1*distinct2
        return res