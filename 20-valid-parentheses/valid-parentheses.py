class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(','{','[']
        closing = [')','}',']']
        st = []
        for ch in s:
            if ch in opening:
                st.append(ch)
            elif ch in closing:
                if len(st)<=0:
                    return False
                c=st.pop()
                if opening.index(c)!=closing.index(ch):
                    return False
        if len(st)==0:
            return True 
        else:
            return False 