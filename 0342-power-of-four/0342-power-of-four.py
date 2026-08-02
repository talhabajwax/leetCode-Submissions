class Solution:
    def isPowerOfFour(self, n: int) -> bool:
    
        if n <= 0:
            return False
        elif n == 1 :
            return True
        while n>1:
            if n%4 != 0:
                return False
            if n%4 == 0:
                n=n//4
        return True
        