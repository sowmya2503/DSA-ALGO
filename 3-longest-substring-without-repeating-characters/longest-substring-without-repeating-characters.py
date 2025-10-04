class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen =0 
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in s[i:j]:
                    break 
                maxlen=max(maxlen,j-i+1)
        return maxlen