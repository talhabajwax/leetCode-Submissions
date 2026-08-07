class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in range(0,len(nums)):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]] = 1
            if count[nums[i]] > 1:
                return True
        else :
            return False
                