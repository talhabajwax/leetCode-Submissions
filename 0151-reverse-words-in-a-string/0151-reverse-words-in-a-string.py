class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse=[]
        for i in range(len(words) - 1, -1, -1) :
            reverse.append(words[i])
        result = " ".join(reverse)
        return result

        