class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Take the first string as a reference for comparison
        prefix = strs[0]

        # Iterate through the remaining strings
        for i in range(1, len(strs)):
            current_string = strs[i]
            # While the current string does not start with the current prefix,
            # shorten the prefix by removing the last character
            while not current_string.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""
        
        return prefix
        