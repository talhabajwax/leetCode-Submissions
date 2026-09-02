class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for t in tokens:
            if t not in "+*-/":
                stack.append(int(t))
            if t in "+*-/":
                right=stack.pop()
                left=stack.pop()
                if t =='+':
                    sol=left+right
                    stack.append(sol)
                if t =='-':
                    sol=left-right
                    stack.append(sol)
                if t =='*':
                    sol=left*right
                    stack.append(sol)
                if t =='/':
                    sol=int(left/right)
                    stack.append(sol)
        return stack.pop()