class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary={}
        for i in range(0,len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]]=i
            elif nums[i] in dictionary:
                l=abs(i-dictionary[nums[i]])
                if l>k:
                    dictionary[nums[i]] = i
                if l<=k:
                    return True
        else :
            return False