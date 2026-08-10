class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output=set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                needed = -(nums[i] + nums[j])
                if needed in seen:
                    triplet = [nums[i], nums[j], needed]
                    triplet.sort()
                    triplet = tuple(triplet)
                    output.add(triplet)
                seen.add(nums[j])
                
        return [list(t) for t in output]
        



#        output=[]
#        for i in range(0,len(nums)):
#            for j in range(i+1,len(nums)):
#                for k in range(j+1,len(nums)):
#                    if nums[i]+nums[j]+nums[k] == 0 :
#                       triplet=[nums[i],nums[j],nums[k]]
#                        triplet.sort()
#                        if triplet not in output:
#                            output.append(triplet)
#        return output