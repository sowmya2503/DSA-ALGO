class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(' ')
        n=[]
        for word in s:
            if word!='':
                n.append(word)
        return ' '.join(reversed(n))
        