class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sort1 = "".join(sorted(s1))
        left=0
        right=len(sort1)
        
        while right<=len(s2):
            sorted_part = "".join(sorted(s2[left:right]))
            if sort1 == sorted_part:
                return True 
                break
            else:
                left+=1
                right+=1
        return False

        