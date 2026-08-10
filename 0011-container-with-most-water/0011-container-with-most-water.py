class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left = 0
        right =len(height)-1
        while left<right:
            width= right-left
            height1= min(height[left],height[right])
            area = width*height1
            if area>max_area:
                max_area=area
            if height[left] <= height[right]:
                left+=1
            elif height[left] >= height[right]:
                right-=1
        return max_area

