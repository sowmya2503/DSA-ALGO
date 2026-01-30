class Solution:
    def palindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1 
        return l+1,r-1
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start,end=0,0
        for i in range(len(s)):
            start1,end1=self.palindrome(s,i,i)
            start2,end2=self.palindrome(s,i,i+1)
            if end1-start1>end-start:
                start,end=start1,end1
            if end2-start2>end-start:
                start,end=start2,end2
        return s[start:end+1]
            
        