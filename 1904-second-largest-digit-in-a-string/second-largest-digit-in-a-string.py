class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        first=-1
        second=-1
        for ch in s:
            if ch.isdigit():
                l.append(int(ch))
        for i in range(len(l)):
            if l[i]>first:
                second=first
                first=l[i]
            elif first>l[i] and l[i]>second:
                second=l[i]
        return second
        