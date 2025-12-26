class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest = sorted(nums,reverse=True)
        new = largest[0:k]
        res=[]
        for num in nums:
            if num in new:
                res.append(num)
                new.remove(num)
            if len(res)==k:
                break 
        return res

