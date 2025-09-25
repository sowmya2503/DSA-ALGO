class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of the number
        is_negative = x < 0
        
        # Work with the absolute value for easier digit manipulation
        num = abs(x)
        
        # Initialize the reversed number
        reversed_num = 0
        
        # Iterate through the digits
        while num > 0:
            # Get the last digit
            last_digit = num % 10
            
            # Build the reversed number
            reversed_num = (reversed_num * 10) + last_digit
            
            # Remove the last digit from the original number
            num //= 10
            
        # Apply the original sign to the reversed number
        if is_negative:
            reversed_num = -reversed_num
            
        # Check for 32-bit signed integer overflow
        # The range is [-2^31, 2^31 - 1]
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        
        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0
        
        return reversed_num