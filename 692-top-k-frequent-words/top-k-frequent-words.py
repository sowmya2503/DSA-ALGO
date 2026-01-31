from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        n=[]
        c=Counter(words)
        l=sorted(c.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            n.append(l[i][0])
        return n

        