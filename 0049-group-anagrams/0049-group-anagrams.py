class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        sort=[]
        for i in range (0,len(strs)):
            word=strs[i]
            key = "".join(sorted(word))
            if key in freq:
                freq[key].append(word)
            else:
                freq[key]=[word]
        for v in freq.values():
            sort.append(v)
        return sort