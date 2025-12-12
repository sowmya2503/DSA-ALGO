from itertools import permutations
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l=[]
        if s1==s2:
            return True
        for i,(c1,c2) in enumerate(zip(s1,s2)):
            if c1!=c2:
                l.append(i)

        if len(l)!=2:
            return False
        #print(l)

        i,j=l
        return s1[i]==s2[j] and s1[j]==s2[i]        