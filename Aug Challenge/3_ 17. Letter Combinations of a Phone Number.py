# problem:
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# solution:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return list(map(''.join, product(*({'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}[digit] for digit in digits)))) if digits else []