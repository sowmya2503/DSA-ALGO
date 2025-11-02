class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        st = s.split(' ')
        for word in st:
            if word!='':
                l.append(word)
                k = ' '.join(reversed(l))
        return k


        