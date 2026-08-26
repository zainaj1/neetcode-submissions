# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        bstList = []
        self.flattenTree(root, bstList)

        return bstList[k-1]


    
    def flattenTree(self, root: Optional[TreeNode], bstList: List) -> List:
        if not root:
            return None

        self.flattenTree(root.left, bstList)
        bstList.append(root.val)
        self.flattenTree(root.right, bstList)
        
        return bstList
    
        
    
        
        