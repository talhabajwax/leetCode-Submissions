class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(0)
            if ch == ')':
                inside = stack.pop()
                if inside == 0:
                    score = 1
                else:
                    score = 2 * inside
                stack[-1] += score
        return stack[-1]