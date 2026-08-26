# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr.left:
            curr = curr.left
        
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                print("for node ", root.val ," returning left: ", root.left)
                return root.left
            elif not root.left:
                print("for node ", root.val ," returning right: ", root.right)
                return root.right
            
            # We can assume minNode exists as we only get to this edge case if there is a root.right
            minNode = self.findMin(root.right)
            minNode.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            
            # Clear deleted node
            root.left = None
            root.right = None
            
            return minNode
        
        return root
                

         
    
        