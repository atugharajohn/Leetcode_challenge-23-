# problem:
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# solution:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        l=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m: l.append(True)
            else: l.append(False)
        return l
        