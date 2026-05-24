class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for ch in s:
            if ch not in d:
                d[ch]=1 
            else:
                d[ch]+=1
        l=[]
        for k,v in d.items():
            if v==1:
                l.append(k)
        if len(l)<1:
            return -1
        minindex=99999
        k=0
        for i in l:
            k=s.index(i)
            minindex=min(minindex,k)
        return minindex
        