class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close=nums[0]+nums[1]+nums[2]
        for i in range(0,len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                add = nums[i]+nums[left]+nums[right]
                if add < target:
                    left+=1
                elif add > target:
                    right -=1
                if add == target:
                    return add
                elif abs(add - target) < abs(close-target):
                    close = add
        return close






#        close=nums[0]+nums[1]+nums[2]
 #       for i in range(0,len(nums)):
  #          for j in range(i+1,len(nums)):
   #             for k in range(j+1,len(nums)):
    #                add = nums[i]+nums[j]+nums[k]
     #               if abs(add - target) < abs(close-target):
      #                  close = add
       #             
        #return close