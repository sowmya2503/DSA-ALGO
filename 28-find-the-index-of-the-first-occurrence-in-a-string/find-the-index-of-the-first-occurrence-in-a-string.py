class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=-1
        try:
            k = haystack.index(needle)
        except:
            pass
        return k
        