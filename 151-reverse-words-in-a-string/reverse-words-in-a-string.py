class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(' ')
        l=[]
        for word in words:
            if word!= '':
                l.append(word)
        k=' '.join(reversed(l))
        return k

        