# problem:
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

# solution:
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        maxSize = 0
        count = collections.Counter()

        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            minCount = min(count['T'], count['F'])

            if minCount <= k:
                maxSize += 1
            
            else:
                count[answerKey[i- maxSize]] -= 1
        return maxSize