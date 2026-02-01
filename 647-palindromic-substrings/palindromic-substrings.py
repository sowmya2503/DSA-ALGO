class Solution:
    def palindrome(self,s,l,r):
        c=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
            c+=1
        return c
    def countSubstrings(self, s: str) -> int:
        c1,c2=0,0
        for i in range(len(s)):
            c1+=self.palindrome(s,i,i+1)
            c2+=self.palindrome(s,i,i)
        return c1+c2

        