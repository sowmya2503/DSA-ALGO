from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=defaultdict(list)
        n=[]
        for word in strs:
            s=''.join(sorted(word))
            l[s].append(word)
        for k,v in l.items():
            n.append(v)
        return n

        
        