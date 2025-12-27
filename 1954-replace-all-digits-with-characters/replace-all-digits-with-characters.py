class Solution:
    def replaceDigits(self, s: str) -> str:
        n=""
        for i in range(1,len(s)):
            if s[i].isdigit():
                char = ord(s[i-1]) + int(s[i])
                newchar = chr(char)
                n+=s[i-1]+newchar
        if not s[-1].isdigit():
            n+=s[-1]
        return n
        