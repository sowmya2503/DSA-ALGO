class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d=defaultdict(list)
        for word in strs:
            k=''.join(sorted(word))
            d[k].append(word)
        return list(d.values())
        