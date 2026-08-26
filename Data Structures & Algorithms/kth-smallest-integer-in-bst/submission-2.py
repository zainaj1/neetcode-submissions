# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    index = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = self.inorderTraverals(root, k)
        
        return num 
    
    def inorderTraverals(self, root: Optional[TreeNode], k: int) -> Optional[int]:
        if not root:
            return None
        
        left_result = self.inorderTraverals(root.left, k)
        
        self.index += 1
        if self.index == k:
            return root.val

        right_result = self.inorderTraverals(root.right, k)
        
        return left_result if left_result else right_result


        

        
    
        
        