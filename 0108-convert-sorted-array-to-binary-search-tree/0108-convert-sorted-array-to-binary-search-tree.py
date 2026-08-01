# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recursion(nums):
            if len(nums) == 0:
                return
            total=len(nums)//2
            left=nums[0:total]
            right=nums[total+1:]
            root = TreeNode(nums[total])
            root.left=recursion(left)
            root.right=recursion(right)
            return root
        return recursion(nums)

