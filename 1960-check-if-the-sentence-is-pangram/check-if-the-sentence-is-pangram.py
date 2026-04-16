class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        from collections import Counter
        d=Counter(sentence)
        if len(d)==26:
            return True
        return False
        