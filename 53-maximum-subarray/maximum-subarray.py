import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        global_max = -math.inf  # Initialize global_max to negative infinity
        current_max = 0         # Initialize current_max to 0

        for num in nums:
            current_max += num
            global_max = max(global_max, current_max)

            # If current_max becomes negative, it's better to start a new subarray
            # from the next element, so reset current_max to 0.
            if current_max < 0:
                current_max = 0
        
        # Handle the case where all numbers are negative.
        # In this scenario, global_max might still be -math.inf if no positive sum was ever found.
        # The true maximum will be the largest single negative number.
        # This is implicitly handled by initializing global_max to -math.inf and current_max to 0.
        # If all numbers are negative, the loop will set global_max to the largest single number
        # when current_max is updated to that negative number.
        # Example: [-2, -1, -3]
        # num = -2: current_max = -2, global_max = -2, current_max = 0
        # num = -1: current_max = -1, global_max = -1, current_max = 0
        # num = -3: current_max = -3, global_max = -1, current_max = 0
        # The final global_max will be -1, which is correct.
        
        # However, a more robust way to handle this explicitly for clarity might be:
        # if max(nums) < 0:
        #     return max(nums)
        # else:
        #     return global_max
        # But the initial Kadane's algorithm setup already handles this correctly.
        
        # A simpler and more common Kadane's implementation for all-negative cases:
        # Initialize both global_max and current_max with the first element, then iterate from the second.
        # This avoids the -math.inf initialization and potential edge case handling.
        # Let's use the more common and robust approach:

        if not nums:
            return 0 # Or raise an error, depending on problem constraints

        global_max = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

        return global_max
