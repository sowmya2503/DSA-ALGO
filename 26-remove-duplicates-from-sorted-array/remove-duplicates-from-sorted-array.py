class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 'insert_index' tracks the position where the next unique element should be placed.
        # It also represents the count of unique elements found so far.
        insert_index = 1 

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous unique element,
            # it means we found a new unique element.
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
        
        # 'insert_index' now holds the count of unique elements, which is also
        # the new length of the array with duplicates removed.
        return insert_index