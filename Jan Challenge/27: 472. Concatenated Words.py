# problem:
# https://leetcode.com/problems/concatenated-words/

# solution:
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        result = []
        def dfs(word, wordset):
            if word == "":
                return True
            for i in range(len(word)):
                if word[:i+1] in wordset:
                    if dfs(word[i+1:], wordset):
                        return True
            return False
        for word in words:
            wordset.remove(word)
            if dfs(word, wordset):
                result.append(word)
            wordset.add(word)
        return result