class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        brack=['(',')']
        output=[]
        current=""
        openn =0
        close=0
        def recursion(current,openn,close):
            if openn == n and close == n:
                output.append(current)
                return 
            if openn < n:
                recursion(current + brack[0], openn + 1, close)
            if close < openn:
                recursion(current + brack[1], openn, close + 1)
        recursion(current,openn,close)
        return output

