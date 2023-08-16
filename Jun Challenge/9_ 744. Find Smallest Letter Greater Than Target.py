# problem:
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# solution:
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        m = max(letters)
        if target >= m: return letters[0]
        for i in letters:
            if i<m and i>target:
                m = i
        return m
