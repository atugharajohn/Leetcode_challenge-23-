# problem:
# https://leetcode.com/problems/string-compression/

# solution:
class Solution:
    def compress(self, chars: List[str]) -> int:
        s=chars[0]
        prev_char=chars[0]
        char_count=1
        for i in chars[1:]:
            if i==prev_char:
                char_count+=1
            else:
                if char_count>1:
                    s+=str(char_count)
                char_count=1
                s+=i
            prev_char=i
        if char_count>1: s+=str(char_count)
        chars[:]=s
        print(s)
        return len(s)