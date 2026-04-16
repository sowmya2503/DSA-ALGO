class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        for k,v in enumerate(words):
            if x in v:
                l.append(k)
        return l

        