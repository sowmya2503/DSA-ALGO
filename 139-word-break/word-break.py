class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        n=len(s)+1
        dp = [False]*n
        dp[0] = True 
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i]=True 
                    break 
        return dp[len(s)]