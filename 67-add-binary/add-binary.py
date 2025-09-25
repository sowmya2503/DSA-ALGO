class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers
        num_a = int(a, 2)
        num_b = int(b, 2)

        # Add the integers
        sum_nums = num_a + num_b

        # Convert the sum back to a binary string
        # The bin() function adds a "0b" prefix, so we slice it off
        return bin(sum_nums)[2:]
