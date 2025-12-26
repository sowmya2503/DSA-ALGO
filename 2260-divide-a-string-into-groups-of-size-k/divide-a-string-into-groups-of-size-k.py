class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if not s:
            return None
        n=[]
        ele=""
        newele=""
        for i in range(0,len(s),k):
            ele=s[i:i+k]
            n.append(ele)
        rem = k-len(n[-1])
        if rem==0:
            return n
        newele+=n[-1]+rem*fill
        n[-1] = newele
        return n