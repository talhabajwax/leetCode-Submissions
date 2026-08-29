class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        freq2={}
        for i in range(0,len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        for j in range(0,len(t)):
            if t[j] in freq2:
                freq2[t[j]]+=1
            else:
                freq2[t[j]]=1
        if freq == freq2:
            return True
        else:
            return False
            
        