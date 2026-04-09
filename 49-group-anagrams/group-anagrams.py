class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        l=[]
        d=defaultdict(list)
        for word in strs:
            k=''.join(sorted(word))
            d[k].append(word)
        for k,v in d.items():
            l.append(v)
        return l
        