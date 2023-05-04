# problem:
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

# solution:
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        res = []
        potions.sort()
        for spell in spells:
            mi = (success + spell - 1) // spell
            res.append(m - bisect_left(potions, mi))
        return res