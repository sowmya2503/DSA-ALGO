class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            prev=res[-1]
            curr=intervals[i]
            if curr[0]<=prev[1]:
                prev[1]=max(curr[1],prev[1])
            else:
                res.append(curr)
        return res
        