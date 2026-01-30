class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res=1
        nums.sort()
        for num in nums:
            if res==num:
                res+=1
            elif num>res:
                break
        return res
        