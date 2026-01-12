class Solution:
    def secondHighest(self, s: str) -> int:
        dig=set()
        for ch in s:
            if ch.isdigit():
                dig.add(int(ch))
        dig=sorted(dig)
        if len(dig)>=2:
            return dig[-2]
        return -1

        '''
        digits = {int(c) for c in s if c.isdigit()}
    
    # Sort the unique digits in descending order
        sorted_digits = sorted(list(digits), reverse=True)
    
    # Return the second element if the list has at least 2 digits
        return sorted_digits[1] if len(sorted_digits) >= 2 else -1
        '''