# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # abs ensures the diff >= 0, so we want to return true if the values are 0 or 1 
        return self.calculateHeight(root)[1]


    """
    We need to compute the balanced property for each subnode to avoid the case where one of the child nodes is not balanced
    and the other is, but the difference between the two childrens hight would imply balance. 

    i.e if the root had a balanced left child with a height of 3, and then the right child had a hight of three but only one left child and multiple children
    in the right child for the right node.
    """
    def calculateHeight(self, root: Optional[TreeNode]) -> (int, bool):
        if not root:
            return (0, True)
       
        left_height = self.calculateHeight(root.left)
        right_height = self.calculateHeight(root.right)

        height = max(left_height[0], right_height[0]) + 1
        balanced = left_height[1] and right_height[1] and abs(left_height[0] - right_height[0]) <= 1
                
        return (height, balanced)
         
        # Equivalent to 
        # left_height = self.calculateHeight(root.left)
        # right_height = self.calculateHeight(root.right)
        # return max(left_height, right_height) + 1
        
       
        
        




        