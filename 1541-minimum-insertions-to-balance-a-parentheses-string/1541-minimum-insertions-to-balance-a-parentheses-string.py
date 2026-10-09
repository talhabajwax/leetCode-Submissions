class Solution:
    def minInsertions(self, s: str) -> int:
        need=0
        insertion=0
        for i in range(0,len(s)):
            if s[i] == '(':
                if need%2 ==1:
                    insertion+=1
                    need-=1
                need += 2
            if s[i] == ')':
                need -= 1
                if need <0:
                    insertion +=1
                    need=1
        return insertion + need