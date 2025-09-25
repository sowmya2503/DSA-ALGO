class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        one = 1  # Represents ways to reach the step before the previous one (i-2)
        two = 1  # Represents ways to reach the previous step (i-1)
        
        for _ in range(n - 1):
            one, two = two, one + two
        
        return two