class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing=[]
        for i in range(0,len(nums)-1):
           if nums[i]+1 != nums[i+1]: 
            m=nums[i]+1
            while m < nums[i+1]: 
                missing.append(m)
                m+=1
            
        return missing

                    
            