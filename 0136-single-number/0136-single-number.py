class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single=[]
        for i in range(0,len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]

        