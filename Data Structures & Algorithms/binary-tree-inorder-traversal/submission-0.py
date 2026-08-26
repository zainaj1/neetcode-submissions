# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        orderedList = []
        self.dfs(orderedList, root)
        return orderedList

    
    def dfs(self, x: List[int], root: Optional[TreeNode]) -> None:
        if not root:
            return None
        
        start = self.dfs(x, root.left)
        x.append(root.val)
        self.dfs(x, root.right)

