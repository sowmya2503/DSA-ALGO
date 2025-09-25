class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index={}
        start=0
        maxlength=0
        maxstring=""
        for index,char in enumerate(s):
            if char in char_index and char_index[char]>=start:
                start=char_index[char]+1 
            char_index[char]=index
            current = index-start+1 
            if current>maxlength:
                maxlength=current
                maxstring=s[start:index+1]

        return maxlength
        