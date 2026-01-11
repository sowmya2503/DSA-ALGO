from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        new=[]
        l=[]
        n = [word.lower() for word in words]
        c = Counter(n)
        l = sorted(c.keys())
        l.sort(key=lambda w:c[w],reverse=True)
        return l[0:k]
      