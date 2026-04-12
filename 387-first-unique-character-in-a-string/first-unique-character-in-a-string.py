class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c=Counter(s)
        for k,v in enumerate(s):
            if c[v]==1:
                return k
        return -1
        