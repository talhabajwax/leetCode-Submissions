class Solution:
    def isPalindrome(self, x: int) -> bool:
        number1= str(x)
        number2=(number1[::-1])
        if number1 == number2:
         return True 
        else: 
         return   False
        