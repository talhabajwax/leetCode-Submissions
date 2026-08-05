class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
       def recursion(index,xor):
        if index==len(nums):
            return xor
        skip=recursion(index+1,xor)
        take=recursion(index+1,xor ^ nums[index])
        return(skip+take)
       return recursion (index=0,xor=0)
 


        