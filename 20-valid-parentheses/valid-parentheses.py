class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(','{','[']
        st=[]
        closing = [')','}',']']
        for ch in s:
            if ch in opening:
                st.append(ch)
            elif ch in closing:
                if len(st)>0:
                    n=st.pop()
                    if closing.index(ch)!=opening.index(n):
                        return False
                elif len(st)==0:
                    return False
        if len(st)==0:
            return True
        return False

        