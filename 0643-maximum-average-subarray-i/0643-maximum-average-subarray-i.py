class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        right=k
        sum1=0
        for i in range(left,right):
            sum1+=nums[i]
        max_sum=sum1
        while right< len(nums):
            sum1=sum1-nums[left]+nums[right]
            left+=1
            right+=1
            if max_sum <sum1:
                max_sum=sum1
        return max_sum/k
