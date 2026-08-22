class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original = n
        n=str(n)
        numSum=0
        numPro=1
        for i in range(len(n)):
            numSum += int(n[i])
            numPro *= int(n[i])
        if original % (numSum + numPro) == 0:
            return True 
        else :
            return False
        
        