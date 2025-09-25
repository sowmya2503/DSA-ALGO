class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the index of the first occurrence of needle in haystack.
        
        Args:
            haystack: The string to search within.
            needle: The substring to search for.
            
        Returns:
            The index of the first occurrence of needle in haystack, 
            or -1 if needle is not part of haystack.
        """
        return haystack.find(needle)
