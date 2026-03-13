class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        n=""
        
        for ch in s:
            if ch.isalnum():
                n+=ch.lower()
        r=len(n)-1
        while l<r:
            if n[l]!=n[r]:
                return False
            l+=1
            r-=1
        return True
        