class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[]
        for i in range (0,len(nums)):
            sq = nums[i] ** 2
            squares.append(sq)
        squares.sort()
        return squares        