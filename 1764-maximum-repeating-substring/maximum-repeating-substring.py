class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        repeated = word
        count=0
        while repeated in sequence:
            repeated+=word
            count+=1
        return count