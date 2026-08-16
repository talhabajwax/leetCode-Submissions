class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters=set()
        max_length =0
        l=0
        r=0
        while r <= len(s)-1:
            if s[r] not in letters:
                letters.add(s[r])
                r += 1
            else:
                letters.remove(s[l])
                l+=1
            max_length = max(max_length, len(letters))
        return max_length
            
        