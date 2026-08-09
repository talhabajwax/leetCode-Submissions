class Solution:
    def isHappy(self, n: int) -> bool:
        sums=set()
        while True:
            digits = []
            for i in str(n):
                digits.append(int(i))
            result=0
            for i in digits:
                result+=i**2
            n=result
            if n==1:
                return True
            if n in sums:
                return False
            if n not in sums:
                sums.add(n)
            
        