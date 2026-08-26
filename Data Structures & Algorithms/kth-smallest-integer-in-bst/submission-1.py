# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    index = 1
    found = False

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = self.inorderTraverals(root, k)
        
        return num 
    
    def inorderTraverals(self, root: Optional[TreeNode], k: int) -> Optional[int]:
        if not root:
            return None
        
        left_result = self.inorderTraverals(root.left, k)
        if self.index == k and not self.found:
            self.found = True
            return root.val
        else:
            self.index += 1
        right_result = self.inorderTraverals(root.right, k)
        
        return left_result if left_result else right_result


        

        
    
        
        