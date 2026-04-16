class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pos,neg=0,0
        if 0 in nums:
            return 0
        for num in nums:
            if num<0:
                neg+=1
            elif num>0:
                pos+=1
        if neg%2==0:
            return 1
        else:
            return -1
        