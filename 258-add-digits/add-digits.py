class Solution:
    def getsum(self,t):
        temp=t
        summ=0
        dig=0
        while temp>0:
                dig = temp%10
                temp=temp//10
                summ+=dig
        return summ
    def addDigits(self, num: int) -> int:
        temp = num 
        
        ans=0
        ans=self.getsum(temp)
        while ans>9:
            ans=self.getsum(ans)
        return ans
        