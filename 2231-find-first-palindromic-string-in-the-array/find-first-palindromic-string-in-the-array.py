class Solution:
    def isPalindrome(self,word):
        l=0
        r=len(word)-1
        while l<r:
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            ans = self.isPalindrome(word)
            if ans:
                return word
        return ""
        