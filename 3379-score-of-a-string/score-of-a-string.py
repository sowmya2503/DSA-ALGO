class Solution:
    def scoreOfString(self, s: str) -> int:
        value=0
        for i in range(1,len(s)):
            v1 = ord(s[i])
            v2 = ord(s[i-1])
            value += abs(v2-v1)
        return value
        