class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            if ch ==')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else :
                    fuck = i - stack[-1]
                    length = max(fuck,length)
        return length