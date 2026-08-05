# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path=[]
        result=[]
        def recursion(root,path):
            path.append(root.val)
            if root.left is None and root.right is None:
                result.append("->".join(map(str, path)))
                return
            if root.left is not None:
                recursion(root.left, path)
                path.pop(-1)
            if root.right is not None:
                recursion(root.right, path)
                path.pop(-1)
        recursion(root, path)
        return result