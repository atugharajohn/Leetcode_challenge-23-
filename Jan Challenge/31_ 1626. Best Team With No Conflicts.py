# problem:
# https://leetcode.com/problems/best-team-with-no-conflicts/

# solution:
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i],ages[i]] for i in range(len(scores))]

        pairs.sort()

        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            mscore , mage = pairs[i]
            for j in range(0,i):
                score,age = pairs[j]
                if mage>=age:
                    dp[i] = max(mscore+dp[j],dp[i])


        return max(dp)  