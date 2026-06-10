class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        k=0
        while k<len(first) and  first[k]==last[k]:
            k+=1
        return first[0:k]    