class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        freq={}
        max_len = 0
        while right <len(s):
            if s[right]  in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            right+=1
            a=max(freq.values())
            replacements = (right - left) - a
            while replacements > k:
                freq[s[left]] -= 1
                left+=1
                a=max(freq.values())
                replacements = (right - left) - a
            current_len = right - left
            if current_len > max_len:
                max_len=current_len
        return max_len