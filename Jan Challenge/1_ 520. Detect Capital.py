# problem:
# https://leetcode.com/problems/detect-capital/

# solution:
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in [word.upper(),word.lower(),word.title()]