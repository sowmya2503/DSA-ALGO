class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]!=target:
                return -1
            return 0
        l=0
        r=len(nums)-1
        mid=0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l+=1
            elif nums[mid]>target:
                r-=1
        return -1
        