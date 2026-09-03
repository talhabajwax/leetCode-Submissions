class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums.reverse()
        left=0
        right=k-1
        left2  = k
        right2 = len(nums) - 1
        while left < right:
            nums[left],nums[right]= nums[right],nums[left]
            left+=1
            right-=1
        while left2 < right2:
            nums[left2],nums[right2]= nums[right2],nums[left2]
            left2+=1
            right2-=1
        