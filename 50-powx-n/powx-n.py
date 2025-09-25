class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current_x = x

        while n > 0:
            # If the current bit of n is 1 (n is odd), multiply result by current_x
            if n % 2 == 1:
                result *= current_x
            
            # Square current_x for the next iteration
            current_x *= current_x
            
            # Right shift n by 1 (equivalent to n // 2)
            n //= 2
            
        return result
