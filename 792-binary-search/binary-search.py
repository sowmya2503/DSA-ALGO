class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2 
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l+=1
            elif nums[mid]>target:
                r-=1
        return -1
        