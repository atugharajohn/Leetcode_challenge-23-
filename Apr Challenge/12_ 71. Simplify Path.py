# problem:
# https://leetcode.com/problems/simplify-path/

# solution:
class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        for i in path.split('/'):
            # print(s)
            if i=='..':
                if s: s.pop()
            elif i not in ['/','.','']:
                s.append(i)
        return '/'+'/'.join(s)