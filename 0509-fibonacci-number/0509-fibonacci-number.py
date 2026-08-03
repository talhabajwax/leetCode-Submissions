class Solution:
    def fib(self, n: int) -> int:
        def recursion(n):
            if n <= 0:
                return n
            if n == 1:
                return n
            if n>1:
                a=n-1
                f1= recursion(a)
                b=n-2
                f2=recursion(b)
                f=f1+f2
                return f
        return recursion (n)        
            
        