'''class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        start = 0
        start1 = start + 1
        while start1 <= len(nums)-1:
            if nums[start] == nums[start1]:
                return nums[start]
            if nums[start] != nums[start1]:
                start1 +=1
            if start1 == len(nums)-1:
                if nums[start] == nums[start1]:
                    return nums[start]
                else:
                    start+=1
                    start1=start+1    '''       
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow     