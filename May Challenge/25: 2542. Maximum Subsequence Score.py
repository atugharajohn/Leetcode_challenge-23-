# problem:
# https://leetcode.com/problems/maximum-subsequence-score/

# solution:
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        d={}
        for i,j in zip(enumerate(nums1),enumerate(nums2)):
            d[(i[1],i[0])]=(j[1],j[0])
            l=sorted(d.keys(),reverse=True,key=lambda x: d[x])
            s=0
            m=float('inf')
            for i in l[:k]:
                m=min(m,d[i][0])
                print(i[0],d[i][0])
            for i in l[:k]:
                s+=i[0]
            return s*m
