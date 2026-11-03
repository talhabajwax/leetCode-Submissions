class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        output=[]
        signs=[]
        for i in range (len(x) - 1,-1,-1):
            if x[i]=='-':
                signs.append(x[i])
            else:
                output.append(x[i])

        output=int(''.join(signs+output))
        if output < -(2**31) or output > (2**31 - 1):
            return 0
        else :
            return output