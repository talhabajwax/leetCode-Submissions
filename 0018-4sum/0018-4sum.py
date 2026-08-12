class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                left=j+1
                right=len(nums)-1
                while left<right:
                    add = nums[i]+nums[j]+nums[left]+nums[right]
                    if add < target:
                        left+=1
                    elif add > target:
                        right -=1
                    if add == target:
                        quadruplet = [nums[i],nums[j],nums[left],nums[right]]
                        quadruplet.sort()
                        quadruplet=tuple(quadruplet)
                        output.add(quadruplet)
                        left += 1
                        right -= 1
        return  [list(t) for t in output]




#        output=[]
#        for i in range(0,len(nums)):
#            for j in range(i+1,len(nums)):
#                for k in range(j+1,len(nums)):
#                    for m in range(k+1,len(nums)):
#                        if  nums[i]+nums[k]+nums[j]+nums[m] == target:
#                            quadruplet = [nums[i],nums[j],nums[k],nums[m]]
#                            quadruplet.sort()
#                            if quadruplet not in output:
#                                output.append(quadruplet)
#        return output
                        
        