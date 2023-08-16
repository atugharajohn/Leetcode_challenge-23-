# problem:
# https://leetcode.com/problems/restore-ip-addresses/

# solution:
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.recurse(s, ans, 0, "", 0)
        return ans
    
    def recurse(self, curr, ans, index, temp, count):
        if count > 4:
            return
        if count == 4 and index == len(curr):
            ans.append(temp)
        for i in range(1, 4):
            if index + i > len(curr):
                break
            s = curr[index:index+i]
            if (s.startswith("0") and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue
            self.recurse(curr, ans, index+i, temp + s + ("." if count < 3 else ""), count+1)