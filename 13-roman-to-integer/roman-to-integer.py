class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            current_value = roman_map[s[i]]
            
            # Check for the subtractive case
            if i < n - 1 and current_value < roman_map[s[i+1]]:
                total -= current_value
            else:
                total += current_value
                
        return total
        