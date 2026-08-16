class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def recursion(expression):
            output=[]
            if not any(op in expression for op in "+-*"):
                output.append(int(expression))
                return output 
            for i in range(0,len(expression)):
                if expression[i] in "+-*":
                    left = expression[:i]
                    right = expression[i+1:]
                    left_results = recursion(left)
                    right_results = recursion(right)
                    for l in left_results:
                        for m in right_results:
                            if expression[i] == '+':
                                output.append(l+m)
                            if expression[i] == '-':
                                output.append(l-m)
                            if expression[i] == '*' :
                                output.append(l*m)
            return output
        return recursion(expression)