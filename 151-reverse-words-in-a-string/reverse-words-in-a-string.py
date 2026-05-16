class Solution:
    def reverseWords(self, s: str) -> str:
        n=[]
        for word in s.split(' '):
            if word:
                n.append(word)
        return ' '.join(reversed(n))
        