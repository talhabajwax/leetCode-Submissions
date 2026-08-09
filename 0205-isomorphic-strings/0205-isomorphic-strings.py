class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        pattern1=[]
        pattern2=[]
        for i in s:
            if i not in dict1:
                dict1[i]=len(dict1)
            pattern1.append(dict1[i])
        for m in t:
            if m not in dict2:
                dict2[m]=len(dict2)
            pattern2.append(dict2[m])
        if pattern1== pattern2:
            return True
        else:
            return False