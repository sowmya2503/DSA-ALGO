class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_occurrence = self._find_first_occurrence(nums, target)
        last_occurrence = self._find_last_occurrence(nums, target)
        return [first_occurrence, last_occurrence]

    def _find_first_occurrence(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        first_idx = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                first_idx = mid  # Potential first occurrence
                high = mid - 1   # Search in the left half for an earlier occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first_idx

    def _find_last_occurrence(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        last_idx = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                last_idx = mid   # Potential last occurrence
                low = mid + 1    # Search in the right half for a later occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last_idx
