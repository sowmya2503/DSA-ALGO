class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        l=[]
        p=permutations(nums)
        for i in p:
            l.append(i)
        return l

        