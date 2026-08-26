# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    index = 0
    res = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = root.val
        self.inorderTraverals(root, k, 0)
        
        return self.res 
    
    def inorderTraverals(self, root: Optional[TreeNode], k: int, index: int) -> Optional[int]:
        if not root:
            return None
        
        self.inorderTraverals(root.left, k, index)
        
        self.index += 1
        if self.index == k:
            self.res = root.val
        
        self.inorderTraverals(root.right, k, index)
        
        return self.res


        

        
    
        
        