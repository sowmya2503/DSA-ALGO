class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n=[]
        j=[]
        for ch in s:
            if ch !='#':
                n.append(ch)
            elif ch=='#':
                if n:
                    n.pop()
        print(n)
        for ch in t:
            if ch !='#':
                j.append(ch)
            elif ch=='#':
                if j:
                    j.pop()
        print(j)
        return n==j